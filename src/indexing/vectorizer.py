from collections import OrderedDict

from src.indexing.tfidf import *
from utilities.export import *
class TfidfVectorizer():
    """
    Transform a list of tokenized document into vectors 
    
    Parameters:
    ----------
    documents: list of lists
        A list of document that need to be tranform into vectors
    
    export: boolean
        Decide if user when to extract idf and tfidf map
    
    Attributes:
    -----------
    idf_map: dictionary(hash map)   
        For storing IDF map

    Methods:
    --------
    fit(documents: list, export: bool = True) -> list:
        Create IDF map from a set of document
    transform(documents: list, export: bool = True) -> list:
        Transform given document(s) into TFIDF vector

    """
    idf_map = OrderedDict()
    def fit(documents: list, export: bool = True) -> list:
        """
        Create IDF from a set of document

        Parameters:
        ---------
        documents: list
            A list of tokenized documents
        export: boolean
            Give option to export IDF map to csv
        """
        idf_map = OrderedDict(sorted(idf(documents).items(), key=lambda t:t[0]))
        if export:
            dict_to_csv(idf_map, "idf_map.csv")
        return list(idf_map.items())
    
    def transform(self, documents: list, export: bool = True) -> list:
        """
        Transform a list of document into a list of vector. Order of vector is the same as input 
        document list

        Parameters:
        -----------
        documents: list of list
            List of tokenized documents
        export: boolean
            Giving option to export transformed document to CSV file
        
        Return:
        -------
        list
            A list of vector with retained order
        """
        result = []
        for document in documents:
            current_vector = OrderedDict()
            current_tf = tf(document)
            for term in self.idf_map.keys():
                if term in document:
                    current_vector[term] = self.idf_map[term] * current_tf[term]
                else:
                    current_vector[term] = 0
            result.append(current_vector)
        return result
