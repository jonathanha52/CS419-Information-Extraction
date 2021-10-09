from textblob import Word

from nltk.stem import WordNetLemmatizer
# use this line to download nltk.wordnet
# nltk.download('wordnet')
wordnet_lemmatizer = WordNetLemmatizer()

#lemmatizer_type = "wordnet" -> WordNetlemmatizer, "textblob" -> TextBlobLemmatizer
#pos = "a" -> adj, "n" -> noun, "v" -> verb
def lemmatize(list_word, lemmatizer_type, pos):
  result = []
  if lemmatizer_type == "wordnet" and pos == "a":
    for word in list_word:
      result.append(wordnet_lemmatizer.lemmatize(word,pos="a"))
  else if lemmatizer_type == "wordnet" and pos == "n":
    for word in list_word:
      result.append(wordnet_lemmatizer.lemmatize(word, pos="n"))
  else if lemmatizer_type == "wordnet" and pos == "v":
    for word in list_word:
      result.append(wordnet_lemmatizer.lemmatize(word, pos="v"))

  else if lemmatizer_type == "textblob" and pos == "a":
    for word in list_word:
      w = Word(word)
      result.append(w.lemmatize("a"))
  else if lemmatizer_type == "textblob" and pos == "v":
    for word in list_word:
      w = Word(word)
      result.append(w.lemmatize("v"))
  else if lemmatizer_type == "textblob" and pos == "n":
    for word in list_word:
      w = Word(word)
      result.append(w.lemmatize("n"))
  return result