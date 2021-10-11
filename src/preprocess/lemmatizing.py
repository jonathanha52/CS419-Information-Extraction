from textblob import Word

from nltk.stem import WordNetLemmatizer
# use this line to download nltk.wordnet
# nltk.download('wordnet')


# lemmatizer_type = "wordnet" -> WordNetlemmatizer, "textblob" -> TextBlobLemmatizer
# pos = "a" -> adj, "n" -> noun, "v" -> verb


def lemmatize(list_word, lemmatizer_type, pos):
    wordnet_lemmatizer = WordNetLemmatizer()
    result = []
    if lemmatizer_type == "wordnet" and pos == "a":
        for word in list_word:
            result.append(wordnet_lemmatizer.lemmatize(word, pos="a"))
    elif lemmatizer_type == "wordnet" and pos == "n":
        for word in list_word:
            result.append(wordnet_lemmatizer.lemmatize(word, pos="n"))
    elif lemmatizer_type == "wordnet" and pos == "v":
        for word in list_word:
            result.append(wordnet_lemmatizer.lemmatize(word, pos="v"))

    elif lemmatizer_type == "textblob" and pos == "a":
        for word in list_word:
            w = Word(word)
            result.append(w.lemmatize("a"))
    elif lemmatizer_type == "textblob" and pos == "v":
        for word in list_word:
            w = Word(word)
            result.append(w.lemmatize("v"))
    elif lemmatizer_type == "textblob" and pos == "n":
        for word in list_word:
            w = Word(word)
            result.append(w.lemmatize("n"))
    return result
