from math import log10

def idf(document_list: list) -> dict:
    """
    Create a IDF map from document list
    Parameters
    ----------
    document_list: list
        List of tokenized document
    """
    N = len(document_list)
    frequency = {}
    idf_map = {}
    for document in document_list:
        for term in set(document):
            if term not in frequency:
                frequency[term] = 1
            else:
                frequency[term] += 1
    for term in frequency.keys():
        idf_map[term] = calc_idf(N, frequency[term])
    return idf_map

def tf(document: list, log: bool = False) -> dict:
    """
    Get term frequency of a tokenized document

    Parameters:
    -----------
    document: list
        List of token of a document
    log: bool
        Use log normalized TF scheme
    """
    frequency = {}
    d = len(document)
    for term in document:
        if term in frequency:
            frequency[term] += 1
        else:
            frequency[term] = 1
    for term in frequency.keys():
        count = frequency[term]
        count = count / d
        if log:
            count = log10(count)
        frequency[term] = count
    return frequency
def calc_idf(N, nt):
    return log10(N/nt)