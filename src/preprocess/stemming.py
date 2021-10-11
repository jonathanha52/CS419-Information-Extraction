def stemming_document(stemmer, document):
    """
    Function for tokenized document, only work with
    single word tokenization in current state of development
    --------------------------------------------
    Parameters
    stemmer: Stemmer from NLTK library.
    document: list
        List of tokens from a document
    """
    return [stemmer.stem(word) for word in document]