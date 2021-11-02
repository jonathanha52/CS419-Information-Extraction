import string


def tokenize_string(file_content):
    word_list = file_content.lower().translate(
        str.maketrans('', '', string.punctuation)).split()
    return word_list
