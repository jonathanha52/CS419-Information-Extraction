from preprocess.tokenize import tokenize_string
from utilities.export import *
from utilities.load_from_folder import *
from preprocess.stemming import *
from indexing.vectorizer import *
from nltk.stem import LancasterStemmer
content = load_json("datasets\\processed\\cran")
text = [x["text"] for x in content]
tokenized = [tokenize_string(x) for x in text]
stemmer = LancasterStemmer()
stemmed = [stemming_document(stemmer, x) for x in tokenized]

vectorizer = TfidfVectorizer()
vectorizer.fit(stemmed)
vectors = vectorizer.transform(stemmed)
vectors_to_csv(vectors, "term.csv")
