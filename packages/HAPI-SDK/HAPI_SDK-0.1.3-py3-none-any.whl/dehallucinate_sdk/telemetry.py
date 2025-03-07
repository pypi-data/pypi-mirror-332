import os
import json
import datetime

def init_telemetry_log(log_path="telemetry.log"):
    if not os.path.exists(log_path):
        with open(log_path, "w") as f:
            f.write("")
    return log_path

def report_usage(license_key, model_id, input_text, output_text, tokenizer, log_path="telemetry.log"):
    #for prod we need to send these metrics as an HTTP call to some sort of server so we can bill properly
    input_tokens = len(tokenizer.tokenize(input_text))
    output_tokens = len(tokenizer.tokenize(output_text))
    usage_data = {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "model_id": model_id,
        "license_key": license_key,  # similarly for prod this should probably be a hashed key/secure etc. 
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
    }
    with open(log_path, "a") as f:
        f.write(json.dumps(usage_data) + "\n")
    print("Telemetry:", usage_data)
    return usage_data
