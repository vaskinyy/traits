from itertools import chain
import unittest
from traits_web_prototype.TraitsEvaluator.ExtendedPunnettSquare import ExtendedPunnetSquare
from traits_web_prototype.TraitsEvaluator.TraitsEvaluator import TraitsEvaluator

__author__ = 'yuriy.vaskin'

######################################################
class BasicTraitsEvaluatorCase(unittest.TestCase):
    def setUp(self):
        pass

class BasicTraitsEvaluatorCase1(BasicTraitsEvaluatorCase):
    def runTest(self):
        trait = 'BLOOD_TYPE'
        mothers_traits = ['I']
        fathers_traits = ['I']
        self.assertEqual(TraitsEvaluator.offspring_probs(trait, mothers_traits, fathers_traits), {'II': 0.0, 'I': 1.0, 'III': 0.0, 'IV': 0.0})

class BasicTraitsEvaluatorCase2(BasicTraitsEvaluatorCase):
    def runTest(self):
        trait = 'EYE_COLOR'
        mothers_traits = ['GREEN']
        fathers_traits = ['BLUE']
        self.assertEqual(TraitsEvaluator.offspring_probs(trait, mothers_traits, fathers_traits), {'BLUE': 0.5, 'BROWN': 0.0, 'GREEN': 0.5})

class BasicTraitsEvaluatorCase3(BasicTraitsEvaluatorCase):
    def runTest(self):
        trait = 'BLOOD_TYPE'
        mothers_traits = ['I', 'II']
        fathers_traits = ['IV']
        self.assertEqual(TraitsEvaluator.offspring_probs(trait, mothers_traits, fathers_traits), {'II': 0.5, 'I': 0.0, 'III': 0.25, 'IV': 0.25})

class BasicTraitsEvaluatorCase4(BasicTraitsEvaluatorCase):
    def runTest(self):
        trait = 'RH_FACTOR'
        mothers_traits = ['PLUS']
        fathers_traits = ['MINUS']
        self.assertEqual(TraitsEvaluator.offspring_probs(trait, mothers_traits, fathers_traits), {'PLUS': 0.5, 'MINUS': 0.5})

class BasicTraitsEvaluatorNegativeCase1(BasicTraitsEvaluatorCase):
    def runTest(self):
        trait = 'asdfsadf'
        mothers_traits = ['PLUS']
        fathers_traits = ['MINUS']

        self.assertEqual(TraitsEvaluator.offspring_probs(trait, mothers_traits, fathers_traits), {})

class BasicTraitsEvaluatorNegativeCase2(BasicTraitsEvaluatorCase):
    def runTest(self):
        trait = 'EYE_COLOR'
        mothers_traits = ['unknown']
        fathers_traits = ['BLUE']

        self.assertEqual(TraitsEvaluator.offspring_probs(trait, mothers_traits, fathers_traits), {'BLUE': 0.25, 'BROWN': 0.5, 'GREEN': 0.25})

class BasicTraitsEvaluatorNegativeCase3(BasicTraitsEvaluatorCase):
    def runTest(self):
        trait = 'EYE_COLOR'
        mothers_traits = ['BLUE']
        fathers_traits = []
        self.assertEqual(TraitsEvaluator.offspring_probs(trait, mothers_traits, fathers_traits), {'BLUE': 0.25, 'BROWN': 0.5, 'GREEN': 0.25})

class BasicTraitsEvaluatorPopulationCase1(BasicTraitsEvaluatorCase):
    def runTest(self):
        trait = 'BITTER_TASTE'
        mothers_traits = ['STRONG_TASTE']
        fathers_traits = ['ALMOST_CANT_TASTE']
        self.assertEqual(TraitsEvaluator.offspring_probs(trait, mothers_traits, fathers_traits), {'STRONG_TASTE': 0.6, 'ALMOST_CANT_TASTE': 0.4})


######################################################
class TraitsPrinter(unittest.TestCase):
    def runTest(self):
        pass
        for name in TraitsEvaluator.get_trait_names():
            trait = TraitsEvaluator.get_trait(name)
            phenotypes = trait.get_phenotypes()
            pairs = []
            print 'Trait %s' % name
            for mp in phenotypes:
                for fp in phenotypes:
                    if (fp, mp) in pairs or (mp, fp) in phenotypes:
                        continue
                    print 'Cross %s x %s' % (mp, fp)
                    print TraitsEvaluator.offspring_probs(trait.name, [mp], [fp])
                    print ''
                    pairs.append((mp, fp))
            print '#########'


######################################################
class TraitsEvaluatorModelCase(unittest.TestCase):
    def setUp(self):
        pass

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


class TraitsEvaluatorModelMapProbabilityGenotypeCorrespondenceByName(TraitsEvaluatorModelCase):
    def runTest(self):
        for name in TraitsEvaluator.get_trait_names():
            trait = TraitsEvaluator.get_trait(name)
            for phenotype in trait.trait_map.keys():
                phenotype_genotypes = trait.trait_map[phenotype]
                if phenotype in trait.phenotype_probs:
                    prob_genotypes = [g for (g, p) in trait.phenotype_probs[phenotype]]
                    for pg in prob_genotypes:
                        self.assertIn(pg, phenotype_genotypes, "Genotype %s of probability map is not in the genotype map of trait %s with phenotype %s" % (pg, name, phenotype))


class TraitsEvaluatorModelProbabilityCorrespondence(TraitsEvaluatorModelCase):
    def runTest(self):
        for name in TraitsEvaluator.get_trait_names():
            trait = TraitsEvaluator.get_trait(name)
            for phenotype in trait.trait_map.keys():
                phenotype_genotypes = trait.trait_map[phenotype]
                if phenotype in trait.phenotype_probs:
                    prob_genotypes = [g for (g, p) in trait.phenotype_probs[phenotype]]
                    for pg in phenotype_genotypes:
                        if pg not in prob_genotypes:
                            self.assertEqual(trait.get_phenotype_probs(pg, phenotype), 1, "Trait %s. Genotype %s of phenotype %s must have 1 probability" % (name, pg, phenotype))
                else:
                    for pg in phenotype_genotypes:
                        self.assertEqual(trait.get_phenotype_probs(pg, phenotype), 1, "Trait %s. Genotype %s of phenotype %s must have 1 probability" % (name, pg, phenotype))


class TraitsEvaluatorModelProbabilitySum(TraitsEvaluatorModelCase):
    def runTest(self):
        for name in TraitsEvaluator.get_trait_names():
            trait = TraitsEvaluator.get_trait(name)
            sums = {}
            for g, p in list(chain.from_iterable(trait.phenotype_probs.values())):
                if g in sums:
                    sums[g] += p
                else:
                    sums[g] = p
            for g in sums.keys():
                self.assertEqual(sums[g], 1, "Trait %s. Sum of probabilities of genotype %s must be 1" % (name, g))


class TraitsEvaluatorModelSharedGenotypesInProbs(TraitsEvaluatorModelCase):
    def runTest(self):
        for name in TraitsEvaluator.get_trait_names():
            trait = TraitsEvaluator.get_trait(name)
            prob_genotypes = [g for (g, p) in list(chain.from_iterable(trait.phenotype_probs.values()))]
            shared_keys = []
            for phenotype in trait.trait_map.iterkeys():
                for g in trait.trait_map[phenotype]:
                    for phenotype1 in trait.trait_map.iterkeys():
                        if phenotype1 != phenotype:
                            if g in trait.trait_map[phenotype1]:
                                shared_keys.append(g)
            for k in shared_keys:
                self.assertIn(k, prob_genotypes, "Trait %s. Genotype %s is shared and must be in probability map" % (name, k))


class TraitsEvaluatorModelFullProbabilitySum(TraitsEvaluatorModelCase):
    def runTest(self):
        for name in TraitsEvaluator.get_trait_names():
            trait = TraitsEvaluator.get_trait(name)
            psquare = ExtendedPunnetSquare(trait)
            prob_map = psquare.get_full_probability_map()
            sum = 0
            for p in  prob_map.itervalues():
                sum += p
            self.assertAlmostEqual(sum, 1.0, 7, "Trait %s. Sum of probabilities of traits must be 1" % (name))



if __name__ == '__main__':
    unittest.main()
