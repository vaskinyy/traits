import unittest
from TraitsEvaluator import *

__author__ = 'yuriy.vaskin'

######################################################
class BasicTraitsEvaluatorCase(unittest.TestCase):
    def setUp(self):
        self.teval = TraitsEvaluator()

class BasicTraitsEvaluatorCase1(BasicTraitsEvaluatorCase):
    def runTest(self):
        trait = 'BLOOD_TYPE'
        mothers_traits = ['I']
        fathers_traits = ['I']
        self.assertEqual(self.teval.offspring_frequencies(trait, mothers_traits, fathers_traits), {'II': 0.0, 'I': 1.0, 'III': 0.0, 'IV': 0.0})

class BasicTraitsEvaluatorCase2(BasicTraitsEvaluatorCase):
    def runTest(self):
        trait = 'EYE_COLOR'
        mothers_traits = ['GREEN']
        fathers_traits = ['BLUE']
        self.assertEqual(self.teval.offspring_frequencies(trait, mothers_traits, fathers_traits), {'BLUE': 0.5, 'BROWN': 0.0, 'GREEN': 0.5})

class BasicTraitsEvaluatorCase3(BasicTraitsEvaluatorCase):
    def runTest(self):
        trait = 'BLOOD_TYPE'
        mothers_traits = ['I', 'II']
        fathers_traits = ['IV']
        self.assertEqual(self.teval.offspring_frequencies(trait, mothers_traits, fathers_traits), {'II': 0.5, 'I': 0.0, 'III': 0.25, 'IV': 0.25})

class BasicTraitsEvaluatorCase4(BasicTraitsEvaluatorCase):
    def runTest(self):
        trait = 'RH_FACTOR'
        mothers_traits = ['PLUS']
        fathers_traits = ['MINUS']
        self.assertEqual(self.teval.offspring_frequencies(trait, mothers_traits, fathers_traits), {'PLUS': 0.5, 'MINUS': 0.5})

class BasicTraitsEvaluatorNegativeCase1(BasicTraitsEvaluatorCase):
    def runTest(self):
        trait = 'asdfsadf'
        mothers_traits = ['PLUS']
        fathers_traits = ['MINUS']

        self.assertEqual(self.teval.offspring_frequencies(trait, mothers_traits, fathers_traits), {})

class BasicTraitsEvaluatorNegativeCase2(BasicTraitsEvaluatorCase):
    def runTest(self):
        trait = 'EYE_COLOR'
        mothers_traits = ['unknown']
        fathers_traits = ['BLUE']

        self.assertEqual(self.teval.offspring_frequencies(trait, mothers_traits, fathers_traits), {'BLUE': 0.25, 'BROWN': 0.5, 'GREEN': 0.25})

class BasicTraitsEvaluatorNegativeCase3(BasicTraitsEvaluatorCase):
    def runTest(self):
        trait = 'EYE_COLOR'
        mothers_traits = ['BLUE']
        fathers_traits = []
        self.assertEqual(self.teval.offspring_frequencies(trait, mothers_traits, fathers_traits), {'BLUE': 0.25, 'BROWN': 0.5, 'GREEN': 0.25})

if __name__ == '__main__':
    unittest.main()
