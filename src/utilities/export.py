import os
import pandas

def dict_to_csv(dict, name):
    root = "datasets\output"
    pd = pandas.DataFrame(dict, index=[0])
    if not os.path.exists(root):
        os.makedirs(root)
    pd.to_csv(os.path.join(root, name))