import os
import glob
import argparse
import lucene
import json
from java.nio.file import Paths
from org.apache.lucene import analysis, document, index, queryparser, search, store


class LuceneIndexer:
    def __init__(self):
        # initialize lucene
        lucene.initVM()
        self.analyzer = analysis.standard.StandardAnalyzer()
        self.directory = store.SimpleFSDirectory(Paths.get('BTTH/Lucene/index_storage/'))
        self.config = index.IndexWriterConfig(self.analyzer)
        self.writer = index.IndexWriter(self.directory, self.config)

    def makeDocument(self,filename):
        # assert os.path.isfile(filename)
        with open(filename, "r") as f:
            content = json.load(f)
        doc = document.Document()
        doc.add(document.StringField("filename", filename, document.Field.Store.YES))
        doc.add(document.TextField("author", content["author"], document.Field.Store.YES))
        doc.add(document.TextField("content", content["text"], document.Field.Store.YES))
        return doc
        
    def addIndex(self,path):
        for filename in glob.glob(os.path.join(path)):
            print("Indexing "+str(filename)+"...")
            doc = self.makeDocument(filename)
            self.writer.addDocument(doc)
        self.writer.close()
        print("Index completed")

if __name__ == "__main__":
    index = LuceneIndexer()
    path = "datasets/processed/cran/*.json"
    index.addIndex(path)
