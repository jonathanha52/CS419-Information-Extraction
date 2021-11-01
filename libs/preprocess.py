import string
from nltk.tokenize import sent_tokenize, word_tokenize
from textblob import TextBlob

from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
import nltk
def get_wordnet_pos(sentence):
    try:
        nltk.data.find("corpora\wordnet.zip")
    except LookupError:
        nltk.download("wordnet")
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    word_and_tag = ([(word, tag_dict.get(nltk.pos_tag([word])[0][1][0].upper(), wordnet.NOUN))
                    for word in nltk.word_tokenize(sentence)])
    return word_and_tag


def get_textblob_pos(sentence):
    tokenized = TextBlob(sentence)
    tag_dict = {"J": 'a',
                "N": 'n',
                "V": 'v',
                "R": 'r'}
    word_and_tag = ([(word, tag_dict.get(pos[0], 'n'))
                    for word, pos in tokenized.tags])
    return word_and_tag
def tokenize_string(file_content):
	word_list = file_content.lower().translate(str.maketrans('', '', string.punctuation)).split()
	return word_list

def lemmatizing_sent(sent, type):
	return

def pos_tag(sent_token):
	return

def term_tokenize(file_content):
	word_list = file_content.lower().translate(str.maketrans('', '', string.punctuation)).split()
	return word_list
def lemmatize(sentence, lemmatizer_type):
    # lemmatizer_type = "wordnet" -> WordNetlemmatizer, "textblob" -> TextBlobLemmatizer
    wordnet_lemmatizer = WordNetLemmatizer()
    result = []
    if lemmatizer_type == "wordnet":
        result = ([wordnet_lemmatizer.lemmatize(
            word, tag) for word, tag in get_wordnet_pos(sentence)])

    elif lemmatizer_type == "textblob":
        result = ([word.lemmatize(tag)
                  for word, tag in get_textblob_pos(sentence)])
    return result
def process(doc, lemma_type):
	result = []
	sents = sent_tokenize(doc)
	for sent in sents:
		lemmas = lemmatize(sent, lemma_type)
		result.append(lemmas)
	return result


from textblob import TextBlob

from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
import nltk
# use these line to download nltk data
# nltk.download('tagsets')
# nltk.download('wordnet')
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')


def get_wordnet_pos(sentence):
    try:
        nltk.data.find("corpora\wordnet.zip")
    except LookupError:
        nltk.download("wordnet")
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    word_and_tag = ([(word, tag_dict.get(nltk.pos_tag([word])[0][1][0].upper(), wordnet.NOUN))
                    for word in nltk.word_tokenize(sentence)])
    return word_and_tag


def get_textblob_pos(sentence):
    tokenized = TextBlob(sentence)
    tag_dict = {"J": 'a',
                "N": 'n',
                "V": 'v',
                "R": 'r'}
    word_and_tag = ([(word, tag_dict.get(pos[0], 'n'))
                    for word, pos in tokenized.tags])
    return word_and_tag


def lemmatize(sentence, lemmatizer_type):
    # lemmatizer_type = "wordnet" -> WordNetlemmatizer, "textblob" -> TextBlobLemmatizer
    wordnet_lemmatizer = WordNetLemmatizer()
    result = []
    if lemmatizer_type == "wordnet":
        result = ([wordnet_lemmatizer.lemmatize(
            word, tag) for word, tag in get_wordnet_pos(sentence)])

    elif lemmatizer_type == "textblob":
        result = ([word.lemmatize(tag)
                  for word, tag in get_textblob_pos(sentence)])
    return result
