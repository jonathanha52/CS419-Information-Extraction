import os
import glob
import argparse
import lucene
from java.nio.file import Paths
from org.apache.lucene import analysis, document, index, queryparser, search, store

class LuceneSearcher:
    def __init__(self):
        lucene.initVM()
        self.analyzer = analysis.standard.StandardAnalyzer()
        self.directory = store.SimpleFSDirectory(Paths.get('BTTH/Lucene/index_storage/'))
        self.reader = index.DirectoryReader.open(self.directory)
        self.searcher = search.IndexSearcher(self.reader)
        # parser = queryparser.classic.QueryParser('text', analyzer)

    def search_author(self, query_str):
        parser = queryparser.classic.QueryParser("author", self.analyzer)
        query = parser.parse(query_string)
        topDocs = self.searcher.search(query, 10) #top 10 close query
        hits = topDocs.scoreDocs
        result = []
        for hit in hits:
            hitDoc = self.searcher.doc(hit.doc)
            result.append(hitDoc.get('filename'))
        return result

    def search_content(self, query_str):
        parser = queryparser.classic.QueryParser("content", self.analyzer)
        query = parser.parse(query_string)
        topDocs = self.searcher.search(query, 10) #top 10 close query
        hits = topDocs.scoreDocs
        result = []
        for hit in hits:
            hitDoc = self.searcher.doc(hit.doc)
            result.append(hitDoc.get('filename'))
        return result
    
if __name__ == "__main__":
    searcher = LuceneSearcher()
    running = True
    while running:
        print("Please choose 1 or 2 for type of query")
        query_type = input("Author(1)|Content(2)")
        query_string = input("Search: ")
        if query_type is None or query_string is None:
            running = False
        elif query_type == "1":
            for x in searcher.search_author(query_string):
                print(x)
            running = False
        elif query_type == "2":
            for x in searcher.search_content(query_string):
                print(x)
            running = False
        