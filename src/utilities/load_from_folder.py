import os
import json
def load_json(path):
    content = []
    files = os.listdir(path)
    for file in files:
        with open(os.path.join(path, file)) as f:
            content.append(json.load(f))
    return content