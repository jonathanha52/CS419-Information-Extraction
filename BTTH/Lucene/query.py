import os
import glob
import argparse
import lucene
from java.nio.file import Paths
from org.apache.lucene import analysis, document, index, queryparser, search, store

class LuceneSearcher:
    def __init__(self):
        lucene.initVM()
        analyzer = analysis.standard.StandardAnalyzer()
        directory = store.SimpleFSDirectory(Paths.get('index_storage/'))
        reader = index.DirectoryReader.open(directory)
        searcher = search.IndexSearcher(reader)
        # parser = queryparser.classic.QueryParser('text', analyzer)

    def search_author(query_str):
        parser = queryparser.classic.QueryParser("author", analyzer)
        query = parser.parse(query_string)
        topDocs = self.searcher.search(query, 10) #chon top 10 doc gan voi query nhat
        hits = topDocs.scoreDocs
        for hit in hits:
            hitDoc = self.searcher.doc(hit.doc)
            yield hitDoc.get('filename')

    def search_author(query_str):
        parser = queryparser.classic.QueryParser("content", analyzer)
        query = parser.parse(query_string)
        topDocs = self.searcher.search(query, 10) #top 10 close query
        hits = topDocs.scoreDocs
        for hit in hits:
            hitDoc = self.searcher.doc(hit.doc)
            yield hitDoc.get('filename')