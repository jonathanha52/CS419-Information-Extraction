import unittest
from math import log10
from src.indexing.tfidf import *

class TfidfUnittest(unittest.TestCase):
    document_list = [
        ["this", "is", "a", "test"],
        ["test", "is", "fun"]
    ]
    expectedIdf = {
        "this": log10(2),
        "is": log10(1),
        "a": log10(2),
        "test": log10(1),
        "fun" : log10(2)
    }
    expectedTf = {
        "this": 1/4,
        "is": 1/4,
        "a": 1/4,
        "test": 1/4
    }
    def testIdf(self):
        self.assertDictEqual(self.expectedIdf, idf(self.document_list))
    def testTf(self):
        self.assertDictEqual(self.expectedTf, tf(self.document_list[0]))