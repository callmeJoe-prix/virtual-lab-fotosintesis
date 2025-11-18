import json

def load_parameters(path):
    with open(path, "r") as f:
        return json.load(f)
