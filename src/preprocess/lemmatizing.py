from textblob import TextBlob, Word


from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
import nltk
# use this line to download nltk data
# nltk.download('wordnet')
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

# lemmatizer_type = "wordnet" -> WordNetlemmatizer, "textblob" -> TextBlobLemmatizer
# pos = "a" -> adj, "n" -> noun, "v" -> verb


def get_wordnet_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)


def get_textblob_pos(word):
    sent = TextBlob(word)
    tag_dict = {"J": 'a',
                "N": 'n',
                "V": 'v',
                "R": 'r'}
    word_and_tag = [(w, tag_dict.get(pos[0], 'n')) for w, pos in sent.tags]
    # lemmatized_word = [wd.lemmatize(tag) for wd, tag in words_and_tags]
    return word_and_tag


def lemmatize(list_word, lemmatizer_type):
    wordnet_lemmatizer = WordNetLemmatizer()
    result = []
    if lemmatizer_type == "wordnet":
        for word in list_word:
            result.append(wordnet_lemmatizer.lemmatize(
                word, get_wordnet_pos(word)))

    elif lemmatizer_type == "textblob":
        for word in list_word:
            word_and_tag = get_textblob_pos(word)
            result.append([w.lemmatize(tag) for w, tag in word_and_tag])
    return result
