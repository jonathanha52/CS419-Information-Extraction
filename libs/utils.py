import json
import os
import pandas


def dict_to_csv(dict, name):
    root = "datasets\output"
    pd = pandas.DataFrame(dict, index=[0])
    if not os.path.exists(root):
        os.makedirs(root)
    pd.to_csv(os.path.join(root, name))


def load_json(path):
    content = []
    files = os.listdir(path)
    for file in files:
        with open(os.path.join(path, file)) as f:
            content.append(json.load(f))
    return content
