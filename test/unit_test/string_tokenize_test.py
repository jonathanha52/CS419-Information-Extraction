import os
import unittest
from src.preprocess.tokenize import *

class TestStringTokenizing(unittest.TestCase):
    test_string  = "this is a test."
    expected = ["this", "is", "a", "test"]
    def testParse(self):
        result = tokenize_string(self.test_string)
        self.assertEqual(self.expected, result)

