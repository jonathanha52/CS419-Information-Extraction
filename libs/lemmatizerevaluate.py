import sys
import os
sys.path.append(os.path.abspath("E:\\UIT\\InformationExtraction\\Github\\CS419-Information-Extraction"))
import timeit
import nltk.data
import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
from nltk import tokenize
from typing_extensions import runtime
import src.preprocess.lemmatizing as lemmatizing
from src.utilities.load_from_folder import load_json
from src.preprocess.tokenize import *


def time_evaluate(lemmatizer_type):
    data_path = "datasets\\processed\\cran"
    contents = load_json(data_path)
    tokenized_contents = []
    f = open("test\\data\\result_"+lemmatizer_type+".txt", "a")
    for content in contents:
        tokenized_contents.append(tokenize.sent_tokenize(content["text"]))
    # print(tokenized_contents[0])
    if(lemmatizer_type == "wordnet"):
        for tokenized_content in tokenized_contents:
            for sentence in tokenized_content:
                for word in lemmatizing.lemmatize(sentence, "wordnet"):
                    f.write(word+" ")
                f.write("\n")
            f.write("\n")
    elif(lemmatizer_type == "textblob"):
        for tokenized_content in tokenized_contents:
            for sentence in tokenized_content:
                for word in lemmatizing.lemmatize(sentence, "textblob"):
                    f.write(word+" ")
                f.write("\n")
            f.write("\n")
    f.close()


if __name__ == "__main__":
    run_time = timeit.timeit("time_evaluate('wordnet')",globals=locals(), number=1)
    print(f"Run time using WordNet lemmatizer on Cranfield datasets is {run_time}")
