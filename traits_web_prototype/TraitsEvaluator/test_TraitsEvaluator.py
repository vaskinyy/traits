from itertools import chain
import unittest
from traits_web_prototype.TraitsEvaluator.ExtendedPunnettSquare import ExtendedPunnetSquare
from traits_web_prototype.TraitsEvaluator.TraitsEvaluator import TraitsEvaluator

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

class BasicTraitsEvaluatorPopulationCase1(BasicTraitsEvaluatorCase):
    def runTest(self):
        trait = 'BITTER_TASTE'
        mothers_traits = ['STRONG_TASTE']
        fathers_traits = ['ALMOST_CANT_TASTE']
        self.assertEqual(self.teval.offspring_frequencies(trait, mothers_traits, fathers_traits), {'STRONG_TASTE': 0.6, 'ALMOST_CANT_TASTE': 0.4})

######################################################
class TraitsEvaluatorModelCase(unittest.TestCase):
    def setUp(self):
        self.teval = TraitsEvaluator()

class TraitsEvaluatorModelAllGenotypesListed(TraitsEvaluatorModelCase):
    def runTest(self):
        for name in TraitsEvaluator.get_trait_names():
            trait = TraitsEvaluator.get_trait(name)
            psquare = ExtendedPunnetSquare(trait)
            genotypes = psquare.get_possible_genotypes()
            for genotype in genotypes:
                self.assertIn(genotype, list(chain.from_iterable(trait.trait_map.values())), "Genotype %s is not in the genotype map of trait %s" % (genotype, name))

class TraitsEvaluatorModelNoUnknownGenotypes(TraitsEvaluatorModelCase):
    def runTest(self):
        for name in TraitsEvaluator.get_trait_names():
            trait = TraitsEvaluator.get_trait(name)
            psquare = ExtendedPunnetSquare(trait)
            trait_genotypes = list(chain.from_iterable(trait.trait_map.values()))
            genotypes = psquare.get_possible_genotypes()
            for genotype in trait_genotypes:
                self.assertIn(genotype, genotypes, "Genotype %s is an impossible genotype of trait %s" % (genotype, name))

class TraitsEvaluatorModelMapProbabilityGenotypeCorrespondence(TraitsEvaluatorModelCase):
    def runTest(self):
        for name in TraitsEvaluator.get_trait_names():
            trait = TraitsEvaluator.get_trait(name)
            trait_genotypes = list(chain.from_iterable(trait.trait_map.values()))
            prob_genotypes = [g for (g, p) in list(chain.from_iterable(trait.phenotype_probs.values()))]
            for pg in prob_genotypes:
                 self.assertIn(pg, trait_genotypes, "Genotype %s of probability map is not in the genotype map of trait %s" % (pg, name))


#bynamecorrespondence
#sum =1
#if shared in map must be in probs
#full freqmap = 1


if __name__ == '__main__':
    unittest.main()
