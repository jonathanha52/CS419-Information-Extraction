import os
import unittest
from src.preprocess.cranfield_parser import *

class TestCranfieldParsing(unittest.TestCase):
    test_path = "test\data\crantest.txt"
    def testParse(self):
        result = cranfield_parser(self.test_path)
        object1 = {
            "title": "experimental investigation of the aerodynamics of a wing in a slipstream .", 
            "author": "brenckman,m.",
            "publisher": "j. ae. scs. 25, 1958, 324.",
            "text": "experimental investigation of the aerodynamics of a wing in a slipstream . an experimental study of a wing in a propeller slipstream was made in order to determine the spanwise distribution of the lift increase due to slipstream at different angles of attack of the wing and at different free stream to slipstream velocity ratios .  the results were intended in part as an evaluation basis for different theoretical treatments of this problem . the comparative span loading curves, together with supporting evidence, showed that a substantial part of the lift increment produced by the slipstream was due to a /destalling/ or boundary-layer-control effect .  the integrated remaining lift increment, after subtracting this destalling lift, was found to agree well with a potential flow theory . an empirical evaluation of the destalling effects was made for the specific configuration of the experiment ."
        }
        self.assertEqual(len(result), 2)
        self.assertDictEqual(result[0], object1)