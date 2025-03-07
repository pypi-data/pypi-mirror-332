import os
import torch
import json
from transformers import LlamaForCausalLM, LlamaTokenizer
from dehallucinate_sdk.config import CLASSIFIER_MAPPING
from dehallucinate_sdk.telemetry import init_telemetry_log, report_usage
from dehallucinate_sdk.utils import extract_hidden_states
from dehallucinate_sdk.classifier import HAPIClassifier  # Assumes classifier.py is available
from dehallucinate_sdk.SE.SemanticEntropy.modules.utils.SE_config import SEConfig
from dehallucinate_sdk.SE.SemanticEntropy.compute_entropy import compute_entropy
from dehallucinate_sdk.SE.utils.init_model import init_model
from dehallucinate_sdk.SE.utils.inference_config import InferenceConfig
from dehallucinate_sdk.SE.ConfidenceFilter.process_tokens import process_tokens, filter_hypotheses
from dehallucinate_sdk.SE.ConfidenceFilter.create_validation import get_topic, generate_validation_prompt
from dehallucinate_sdk.SE.ConfidenceFilter.extract_keywords import extract_keywords
from dehallucinate_sdk.SE.SelfContradiction.self_contradiction import check_contradiction
from dehallucinate_sdk.SE.CoNLI.modules.data.response_preprocess import hypothesis_preprocess_into_sentences
from concurrent.futures import ThreadPoolExecutor
from huggingface_hub import login

# Log in to Hugging Face if needed (this line can be removed if clients set tokens themselves)
login(token="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")

se_config = SEConfig()
inference_config = InferenceConfig()

class DeHallucinationClient:
    def __init__(self, model_id, license_key, openai_api_key=None, hf_api_key=None, device="cuda:0", telemetry_log_path="telemetry.log"):
        """
        Initializes the dehallucination client.
        :param model_id: Hugging Face model identifier (e.g., "meta-llama/Llama-2-7b-chat-hf")
        :param license_key: Client’s license key.
        :param openai_api_key: The OpenAI API key. If not provided, will fall back to the OPENAI_API_KEY environment variable.
        :param hf_api_key: The Hugging Face API token. If not provided, will fall back to the HUGGINGFACE_API_KEY environment variable.
        :param device: Device to use ("cuda:0" if GPU available, otherwise "cpu").
        :param telemetry_log_path: Path for logging telemetry data.
        """
        if not license_key or license_key.strip() == "":
            raise ValueError("A valid license key is required.")
        self.license_key = license_key
        self.model_id = model_id
        self.device = device if torch.cuda.is_available() else "cpu"
        
        # Set OpenAI API key: client can pass it directly, or it will be taken from the environment.
        if openai_api_key is None:
            openai_api_key = os.environ.get("OPENAI_API_KEY")
        if not openai_api_key:
            raise ValueError("An OpenAI API key is required either as a parameter or via the OPENAI_API_KEY environment variable.")
        self.openai_api_key = openai_api_key
        
        # Set Hugging Face API token similarly.
        if hf_api_key is None:
            hf_api_key = os.environ.get("HUGGINGFACE_API_KEY")
        if not hf_api_key:
            raise ValueError("A Hugging Face API token is required either as a parameter or via the HUGGINGFACE_API_KEY environment variable.")
        self.hf_api_key = hf_api_key

        # Load LLM from Hugging Face, using the provided HF token.
        print(f"Loading LLM ({model_id}) on {self.device}...")
        self.tokenizer = LlamaTokenizer.from_pretrained(model_id, use_auth_token=self.hf_api_key)
        self.model = LlamaForCausalLM.from_pretrained(
            model_id, 
            torch_dtype=torch.float16,  # enforce half precision
            device_map="auto",
            offload_folder="./offload",
            use_auth_token=self.hf_api_key
        )

        # Load classifier based on the model ID.
        if model_id not in CLASSIFIER_MAPPING:
            raise ValueError(f"No classifier configured for model_id '{model_id}'")
        classifier_path = CLASSIFIER_MAPPING[model_id]
        print("Loading Hallucination Classifier from", classifier_path)
        self.classifier = HAPIClassifier(classifier_path, device=self.device)

        # Initialize telemetry logging.
        self.telemetry_log_path = init_telemetry_log(telemetry_log_path)
        print("DeHallucinationClient initialized")

    def generate_sentence(self, context, sentence_max_length=60, temperature=0.8, top_k=50, semantic_entropy=False):
        print("Generating sentence...")
        inputs = self.tokenizer(context, return_tensors="pt").to(self.device)
        
        return_dict_in_generate = semantic_entropy
        output_scores = semantic_entropy

        output = self.model.generate(
            **inputs,
            max_new_tokens=sentence_max_length,
            do_sample=True,
            temperature=temperature,
            top_k=top_k,
            return_dict_in_generate=return_dict_in_generate,
            output_scores=output_scores,
        )

        if return_dict_in_generate:
            sequences = output.sequences
            scores = output.scores
        else:
            sequences = output
            scores = None

        sentence = self.tokenizer.decode(sequences[0], skip_special_tokens=True)
        if sentence.startswith(context):
            sentence = sentence[len(context):].strip()
        if ". " in sentence:
            sentence = sentence.split(". ")[0] + "."
        else:
            if sentence and sentence[-1] not in ".!?":
                sentence += "."
                
        print(sentence)

        if semantic_entropy and scores is not None:
            generated_tokens = sequences[0, inputs.input_ids.shape[-1]:]
            probs = [torch.softmax(score, dim=-1) for score in scores]
            token_probs = []
            token_texts = []
            for i, token_id in enumerate(generated_tokens):
                token_probs.append(probs[i][0, token_id].item())
                token_text = self.tokenizer.decode([token_id.item()])
                token_texts.append(token_text)
            return sentence.strip(), token_probs, token_texts
        
        return sentence.strip(), None, None

    def sentence_contains_hallucination(self, sentence, original_prompt, threshold=0.9):
        print("Checking hallucination...")
        stripped_sentence = sentence.replace(original_prompt, "").replace("\n", " ").strip()
        tokens = stripped_sentence.split()
        for token in tokens:
            token_tensor = self.tokenizer(token, return_tensors="pt").input_ids.to(self.device)
            hidden_state = extract_hidden_states(self.model, token_tensor)
            score = self.classifier.get_hallucination_score(hidden_state)
            if score > threshold:
                return True
        return False

    def semantic_entropy_check(self, sentence, original_prompt, tokens_raw, probs_raw):
        print("Analyzing semantic entropy...")
        try:
            entropies, _ = compute_entropy(se_config, self.openai_api_key, "", [(sentence, probs_raw, tokens_raw)])
            semantic_entropy_score = entropies.get("semantic_entropy", [0])[0]
        except Exception as e:
            print("Error computing semantic entropy:", e)
            semantic_entropy_score = 0.0
        is_hallucinated_se = semantic_entropy_score > se_config.entropy_threshold
        return {"semantic_entropy": semantic_entropy_score, "is_hallucinated_se": is_hallucinated_se}

    def dehallucinate1(self, prompt, desired_word_count=250, sentence_max_length=60, max_regen_attempts=5, threshold=0.9):
        """
        dehallucinate1: Generates a passage using only the classifier-based approach.
        """
        context = prompt
        generated_sentences = []
        flagged_sentences = []
        while len(" ".join(generated_sentences).split()) < desired_word_count:
            sentence = self.generate_sentence(context, sentence_max_length, semantic_entropy=False)[0]
            attempts = 0
            while self.sentence_contains_hallucination(sentence, prompt, threshold) and attempts < max_regen_attempts:
                print(f"[dehallucinate1] Hallucination detected in sentence: '{sentence}'. Regenerating (attempt {attempts+1})...")
                flagged_sentences.append(sentence)
                sentence = self.generate_sentence(context, sentence_max_length, semantic_entropy=False)[0]
                attempts += 1
            generated_sentences.append(sentence)
            context += " " + sentence
            if not sentence.strip():
                break
        output_text = " ".join(generated_sentences)
        report_usage(self.license_key, self.model_id, prompt, output_text, self.tokenizer, self.telemetry_log_path)
        return output_text, flagged_sentences

    def dehallucinate2(self, prompt, desired_word_count=250, sentence_max_length=60, max_regen_attempts=5, threshold=0.9):
        """
        dehallucinate2: Generates a passage using classifier plus semantic entropy filtering.
        """
        context = prompt
        generated_sentences = []
        flagged_sentences = []
        se_flags = []
        while len(" ".join(generated_sentences).split()) < desired_word_count:
            sentence, token_probs, tokens_raw = self.generate_sentence(context, sentence_max_length, semantic_entropy=True)
            attempts = 0
            while self.sentence_contains_hallucination(sentence, prompt, threshold) and attempts < max_regen_attempts:
                print(f"[dehallucinate2] Classifier flagged sentence: '{sentence}'. Regenerating (attempt {attempts+1})...")
                flagged_sentences.append(sentence)
                sentence, token_probs, tokens_raw = self.generate_sentence(context, sentence_max_length, semantic_entropy=True)
                attempts += 1
            # Perform semantic entropy check
            se_result = self.semantic_entropy_check(sentence, prompt, tokens_raw, token_probs)
            if se_result["is_hallucinated_se"]:
                print(f"[dehallucinate2] Semantic entropy flagged sentence: '{sentence}'. Regenerating...")
                flagged_sentences.append(sentence)
                continue  # Skip this sentence; optionally, you could reattempt regeneration here.
            generated_sentences.append(sentence)
            context += " " + sentence
            if not sentence.strip():
                break
            se_flags.append(se_result)
        output_text = " ".join(generated_sentences)
        report_usage(self.license_key, self.model_id, prompt, output_text, self.tokenizer, self.telemetry_log_path)
        return output_text, flagged_sentences, se_flags

    def full_generation(self, prompt, max_length=400):
        print("Generating full output...")
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        output_ids = self.model.generate(**inputs, max_length=max_length)
        output_text = self.tokenizer.decode(output_ids[0], skip_special_tokens=True)
        report_usage(self.license_key, self.model_id, prompt, output_text, self.tokenizer, self.telemetry_log_path)
        return output_text
