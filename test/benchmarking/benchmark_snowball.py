import timeit
from src.preprocess.stemming import *
from src.preprocess.tokenize import *
from src.utilities.load_from_folder import load_json
from memory_profiler import profile
from nltk.stem.snowball import SnowballStemmer
@profile
def benchmark_stemming_snowball():
    data_path = "datasets\\processed\\cran"
    contents = load_json(data_path)
    tokenized_contents = []
    for content in contents:
        tokenized_contents.append(tokenize_string(content["text"]))
    stemmer = SnowballStemmer("english")
    for tokenized_content in tokenized_contents:
        stemming_document(stemmer, tokenized_content)

if __name__ == "__main__":
    run_time = timeit.timeit("benchmark_stemming_snowball()", globals=locals(), number=1)
    print(f"Run time using Snowball stemmer on Cranfield datasets is {run_time}")

