import unittest
from ExtendedPunnettSquare import *
from TraitsGenotypeMaps import *
from TraitsEvaluator import *

__author__ = 'yuriy.vaskin'

######################################################
class SimpleExtendedSquareTestCase(unittest.TestCase):
    def setUp(self):
        self.psquare = ExtendedPunnetSquare()
        self.psquare.fathers_genes = ['A', 'B']
        self.psquare.mothers_genes = ['A', 'A']

class BaseGetFrequency1(SimpleExtendedSquareTestCase):
    def runTest(self):
        self.assertEqual(self.psquare.get_genotype_frequency('AA'), 0.5)

class BaseGetFrequency2(SimpleExtendedSquareTestCase):
    def runTest(self):
        self.assertEqual(self.psquare.get_genotype_frequency('AB'), 0.5)

class BaseGetFrequency3(SimpleExtendedSquareTestCase):
    def runTest(self):
        self.assertEqual(self.psquare.get_genotype_frequency('BA'), 0)

######################################################
class StandardSquareTestCase(unittest.TestCase):
    def setUp(self):
        self.psquare = ExtendedPunnetSquare()
        self.psquare.fathers_genes = ['A', 'a']
        self.psquare.mothers_genes = ['B', 'b']

class StandardGetFrequency1(StandardSquareTestCase):
    def runTest(self):
        self.assertEqual(self.psquare.get_genotype_frequency('AB'), 0.25)

class StandardGetFrequency2(StandardSquareTestCase):
    def runTest(self):
        self.assertEqual(self.psquare.get_genotype_frequency('Ab'), 0.25)

class StandardGetFrequency3(StandardSquareTestCase):
    def runTest(self):
        self.go = GenotypeOperator()
        self.assertEqual(self.psquare.get_genotype_frequency(self.go.get_lexicographic_string('aB')), 0.25)

class StandardGetFrequency4(StandardSquareTestCase):
    def runTest(self):
        self.go = GenotypeOperator()
        self.assertEqual(self.psquare.get_genotype_frequency(self.go.get_lexicographic_string('ab')), 0.25)

class StandardGetFrequency5(StandardSquareTestCase):
    def runTest(self):
        self.go = GenotypeOperator()
        self.assertEqual(self.psquare.get_genotype_frequency(self.go.get_lexicographic_string('Aa')), 0)

######################################################
class SimpleExtendedSquareEmpty(unittest.TestCase):
    def setUp(self):
        self.psquare = ExtendedPunnetSquare()
        self.psquare.fathers_genes = []
        self.psquare.mothers_genes = []
    def runTest(self):
        self.assertEqual(self.psquare.get_genotype_frequency('BA'), 0)

class SimpleExtendedSquareEmpty1(unittest.TestCase):
    def setUp(self):
        self.psquare = ExtendedPunnetSquare()
        self.psquare.fathers_genes = ['a']
        self.psquare.mothers_genes = []
    def runTest(self):
        self.assertEqual(self.psquare.get_genotype_frequency('a'), 0)

class SimpleExtendedSquareEmpty2(unittest.TestCase):
    def setUp(self):
        self.psquare = ExtendedPunnetSquare()
        self.psquare.fathers_genes = []
        self.psquare.mothers_genes = ['a']
    def runTest(self):
        self.assertEqual(self.psquare.get_genotype_frequency('a'), 0)

######################################################
class LexicographicTestCase1(unittest.TestCase):
    def runTest(self):
        s = 'aA'
        self.go = GenotypeOperator()
        self.assertEqual(self.go.get_lexicographic_string(s), 'Aa')

class LexicographicTestCase2(unittest.TestCase):
    def runTest(self):
        s = 'aAb'
        self.go = GenotypeOperator()
        self.assertEqual(self.go.get_lexicographic_string(s), 'Aab')

class LexicographicTestCase3(unittest.TestCase):
    def runTest(self):
        s = 'aaaAAA'
        self.go = GenotypeOperator()
        self.assertEqual(self.go.get_lexicographic_string(s), 'AAAaaa')

######################################################
class GenotypeOperatorTestCase(unittest.TestCase):
    def setUp(self):
        self.go = GenotypeOperator()
class CrossGenotypeTestCase1(GenotypeOperatorTestCase):
    def runTest(self):
        g1='A'
        g2='b'
        self.assertEqual(self.go.cross_genotypes(g1,g2), 'Ab')

class CrossGenotypeTestCase2(GenotypeOperatorTestCase):
    def runTest(self):
        g1='b'
        g2='A'
        self.assertEqual(self.go.cross_genotypes(g1,g2), 'Ab')

class CrossGenotypeTestCase3(GenotypeOperatorTestCase):
    def runTest(self):
        g1='A,a'
        g2='B,b'
        self.assertEqual(self.go.cross_genotypes(g1,g2), 'AB,ab')

class CrossGenotypeTestCase4(GenotypeOperatorTestCase):
    def runTest(self):
        g1='b'
        g2='B,b'
        self.assertEqual(self.go.cross_genotypes(g1,g2), ',Bbb')


######################################################
class BuildSquareFromMapTestCase(unittest.TestCase):
    def setUp(self):
        self.psquare = ExtendedPunnetSquare()
        self.psquare.set_trait(Trait(trait_map={'PT1':['AA,xx'], 'PT2' : ['BB,yy']}))

class BuildSquareFromMapCase1(BuildSquareFromMapTestCase):
    def runTest(self):
        self.assertEqual(self.psquare.get_genotype_frequency('BB,yy'), 0.0625)

class BuildSquareFromMapCase2(BuildSquareFromMapTestCase):
    def runTest(self):
        self.assertEqual(self.psquare.get_genotype_frequency('AB,xy'), 0.25)

######################################################
class ReduceByPhenotypeTestCase(unittest.TestCase):
    def setUp(self):
        self.psquare = ExtendedPunnetSquare()
        self.psquare.set_trait(TraitsEvaluator.get_trait('BLOOD_TYPE'))

class ReduceByPhenotypeTestCase1(ReduceByPhenotypeTestCase):
    def runTest(self):
        self.psquare.reduce_by_mothers_traits(['I'])
        self.psquare.reduce_by_fathers_traits(['I'])
        self.assertEqual(self.psquare.get_genotype_frequency('OO'), 1.0)
######################################################
class BadPhenotypeTestCase1(unittest.TestCase):
    def setUp(self):
        self.psquare = ExtendedPunnetSquare()
        self.psquare.set_trait(TraitsEvaluator.get_trait('EYE_COLOR'))
    def runTest(self):
        self.psquare.reduce_by_mothers_traits(['BROWN'])
        self.psquare.reduce_by_fathers_traits(['ASF'])
        self.assertEqual(self.psquare.get_full_probability_map(), {'BLUE': 0.0625, 'BROWN': 0.75, 'GREEN': 0.1875})

class BadPhenotypeTestCase2(unittest.TestCase):
    def setUp(self):
        self.psquare = ExtendedPunnetSquare()
        self.psquare.set_trait(TraitsEvaluator.get_trait('BLOOD_TYPE'))
    def runTest(self):
        fmap_all_genotypes = self.psquare.get_full_probability_map()
        self.psquare.reduce_by_mothers_traits(['gfdsg'])
        self.psquare.reduce_by_fathers_traits(['asdf'])
        self.assertEqual(self.psquare.get_full_probability_map(), fmap_all_genotypes)

######################################################
class BloodTypeFrequencyMapTestCase(unittest.TestCase):
    def setUp(self):
        self.psquare = ExtendedPunnetSquare()
        self.psquare.set_trait(TraitsEvaluator.get_trait('BLOOD_TYPE'))

class BloodTypeFrequencyMapTestCase1(BloodTypeFrequencyMapTestCase):
    def runTest(self):
        self.psquare.reduce_by_mothers_traits(['I'])
        self.psquare.reduce_by_fathers_traits(['I'])
        self.assertEqual(self.psquare.get_full_probability_map(), {'II': 0.0, 'I': 1.0, 'III': 0.0, 'IV': 0.0})

class BloodTypeFrequencyMapTestCase2(BloodTypeFrequencyMapTestCase):
    def runTest(self):
        self.psquare.reduce_by_mothers_traits(['I'])
        self.psquare.reduce_by_fathers_traits(['II'])
        self.assertEqual(self.psquare.get_full_probability_map(), {'II': 0.5, 'I': 0.5, 'III': 0.0, 'IV': 0.0})

class BloodTypeFrequencyMapTestCase3(BloodTypeFrequencyMapTestCase):
    def runTest(self):
        self.psquare.reduce_by_mothers_traits(['I'])
        self.psquare.reduce_by_fathers_traits(['III'])
        self.assertEqual(self.psquare.get_full_probability_map(), {'II': 0.0, 'I': 0.5, 'III': 0.5, 'IV': 0.0})

class BloodTypeFrequencyMapTestCase4(BloodTypeFrequencyMapTestCase):
    def runTest(self):
        self.psquare.reduce_by_mothers_traits(['I'])
        self.psquare.reduce_by_fathers_traits(['IV'])
        self.assertEqual(self.psquare.get_full_probability_map(), {'II': 0.5, 'I': 0.0, 'III': 0.5, 'IV': 0.0})

class BloodTypeFrequencyMapTestCase5(BloodTypeFrequencyMapTestCase):
    def runTest(self):
        self.psquare.reduce_by_mothers_traits(['II'])
        self.psquare.reduce_by_fathers_traits(['II'])
        self.assertEqual(self.psquare.get_full_probability_map(), {'II': 0.75, 'I': 0.25, 'III': 0.0, 'IV': 0.0} )

class BloodTypeFrequencyMapTestCase6(BloodTypeFrequencyMapTestCase):
    def runTest(self):
        self.psquare.reduce_by_mothers_traits(['II'])
        self.psquare.reduce_by_fathers_traits(['III'])
        self.assertEqual(self.psquare.get_full_probability_map(), {'II': 0.25, 'I': 0.25, 'III': 0.25, 'IV': 0.25})

class BloodTypeFrequencyMapTestCase7(BloodTypeFrequencyMapTestCase):
    def runTest(self):
        self.psquare.reduce_by_mothers_traits(['II'])
        self.psquare.reduce_by_fathers_traits(['IV'])
        self.assertEqual(self.psquare.get_full_probability_map(), {'II': 0.5, 'I': 0.0, 'III': 0.25, 'IV': 0.25})

class BloodTypeFrequencyMapTestCase8(BloodTypeFrequencyMapTestCase):
    def runTest(self):
        self.psquare.reduce_by_mothers_traits(['III'])
        self.psquare.reduce_by_fathers_traits(['III'])
        self.assertEqual(self.psquare.get_full_probability_map(), {'II': 0.0, 'I': 0.25, 'III': 0.75, 'IV': 0.0})

class BloodTypeFrequencyMapTestCase9(BloodTypeFrequencyMapTestCase):
    def runTest(self):
        self.psquare.reduce_by_mothers_traits(['III'])
        self.psquare.reduce_by_fathers_traits(['IV'])
        self.assertEqual(self.psquare.get_full_probability_map(), {'II': 0.25, 'I': 0.0, 'III': 0.5, 'IV': 0.25})

class BloodTypeFrequencyMapTestCase10(BloodTypeFrequencyMapTestCase):
    def runTest(self):
        self.psquare.reduce_by_mothers_traits(['IV'])
        self.psquare.reduce_by_fathers_traits(['IV'])
        self.assertEqual(self.psquare.get_full_probability_map(), {'II': 0.25, 'I': 0.0, 'III': 0.25, 'IV': 0.5})

######################################################
class EyeColorFrequencyMapTestCase(unittest.TestCase):
    def setUp(self):
        self.psquare = ExtendedPunnetSquare()
        self.psquare.set_trait(TraitsEvaluator.get_trait('EYE_COLOR'))

class EyeColorFrequencyMapTestCase1(EyeColorFrequencyMapTestCase):
    def runTest(self):
        self.psquare.reduce_by_mothers_traits(['BROWN'])
        self.psquare.reduce_by_fathers_traits(['BROWN'])
        self.assertEqual(self.psquare.get_full_probability_map(), {'BLUE': 0.0625, 'BROWN': 0.75, 'GREEN': 0.1875})

class EyeColorFrequencyMapTestCase2(EyeColorFrequencyMapTestCase):
    def runTest(self):
        self.psquare.reduce_by_mothers_traits(['GREEN'])
        self.psquare.reduce_by_fathers_traits(['BROWN'])
        self.assertEqual(self.psquare.get_full_probability_map(), {'BLUE': 0.125, 'BROWN': 0.5, 'GREEN': 0.375})

class EyeColorFrequencyMapTestCase3(EyeColorFrequencyMapTestCase):
    def runTest(self):
        self.psquare.reduce_by_mothers_traits(['BLUE'])
        self.psquare.reduce_by_fathers_traits(['BROWN'])
        self.assertEqual(self.psquare.get_full_probability_map(), {'BLUE': 0.25, 'BROWN': 0.5, 'GREEN': 0.25})

class EyeColorFrequencyMapTestCase4(EyeColorFrequencyMapTestCase):
    def runTest(self):
        self.psquare.reduce_by_mothers_traits(['GREEN'])
        self.psquare.reduce_by_fathers_traits(['GREEN'])
        self.assertEqual(self.psquare.get_full_probability_map(), {'BLUE': 0.25, 'BROWN': 0.0, 'GREEN': 0.75})

class EyeColorFrequencyMapTestCase5(EyeColorFrequencyMapTestCase):
    def runTest(self):
        self.psquare.reduce_by_mothers_traits(['GREEN'])
        self.psquare.reduce_by_fathers_traits(['BLUE'])
        self.assertEqual(self.psquare.get_full_probability_map(), {'BLUE': 0.5, 'BROWN': 0.0, 'GREEN': 0.5})

class EyeColorFrequencyMapTestCase6(EyeColorFrequencyMapTestCase):
    def runTest(self):
        self.psquare.reduce_by_mothers_traits(['BLUE'])
        self.psquare.reduce_by_fathers_traits(['BLUE'])
        self.assertEqual(self.psquare.get_full_probability_map(), {'BLUE': 1.0, 'BROWN': 0.0, 'GREEN': 0.0})

######################################################
class RhFactorFrequencyMapTestCase(unittest.TestCase):
    def setUp(self):
        self.psquare = ExtendedPunnetSquare()
        self.psquare.set_trait(TraitsEvaluator.get_trait('RH_FACTOR'))

class RhFactorFrequencyMapTestCase1(RhFactorFrequencyMapTestCase):
    def runTest(self):
        self.psquare.reduce_by_mothers_traits(['PLUS'])
        self.psquare.reduce_by_fathers_traits(['PLUS'])
        self.assertEqual(self.psquare.get_full_probability_map(), {'PLUS': 0.75, 'MINUS': 0.25} )

class RhFactorFrequencyMapTestCase2(RhFactorFrequencyMapTestCase):
    def runTest(self):
        self.psquare.reduce_by_mothers_traits(['PLUS'])
        self.psquare.reduce_by_fathers_traits(['MINUS'])
        self.assertEqual(self.psquare.get_full_probability_map(), {'PLUS': 0.5, 'MINUS': 0.5})

class RhFactorFrequencyMapTestCase3(RhFactorFrequencyMapTestCase):
    def runTest(self):
        self.psquare.reduce_by_mothers_traits(['MINUS'])
        self.psquare.reduce_by_fathers_traits(['MINUS'])
        self.assertEqual(self.psquare.get_full_probability_map(), {'PLUS': 0.0, 'MINUS': 1.0} )


######################################################
class HairColorFrequencyMapTestCase(unittest.TestCase):
    def setUp(self):
        self.psquare = ExtendedPunnetSquare()
        self.psquare.set_trait(TraitsEvaluator.get_trait('HAIR_COLOR'))

class HairColorFrequencyMapTestCase1(HairColorFrequencyMapTestCase):
    def runTest(self):
        self.psquare.reduce_by_mothers_traits(['BLACK'])
        self.psquare.reduce_by_fathers_traits(['BLACK'])
        self.assertEqual(self.psquare.get_full_probability_map(), {'STRAWBERRY_BLOND': 0.0, 'BLACK': 1.0, 'BLOND': 0.0, 'RED': 0.0, 'BROWN': 0.0} )

class HairColorFrequencyMapTestCase2(HairColorFrequencyMapTestCase):
    def runTest(self):
        self.psquare.reduce_by_mothers_traits(['RED'])
        self.psquare.reduce_by_fathers_traits(['RED'])
        self.assertEqual(self.psquare.get_full_probability_map(), {'STRAWBERRY_BLOND': 0.0, 'BLACK': 0.0, 'BLOND': 0.0, 'RED': 1.0, 'BROWN': 0.0} )

class HairColorFrequencyMapTestCase3(HairColorFrequencyMapTestCase):
    def runTest(self):
        self.psquare.reduce_by_mothers_traits(['BLOND'])
        self.psquare.reduce_by_fathers_traits(['BLOND'])
        self.assertEqual(self.psquare.get_full_probability_map(), {'STRAWBERRY_BLOND': 0.0, 'BLACK': 0.0, 'BLOND': 1.0, 'RED': 0.0, 'BROWN': 0.0} )

class HairColorFrequencyMapTestCase4(HairColorFrequencyMapTestCase):
    def runTest(self):
        self.psquare.reduce_by_mothers_traits(['STRAWBERRY_BLOND'])
        self.psquare.reduce_by_fathers_traits(['STRAWBERRY_BLOND'])
        self.assertEqual(self.psquare.get_full_probability_map(), {'STRAWBERRY_BLOND': 0.5, 'BLACK': 0.0, 'BLOND': 0.25, 'RED': 0.25, 'BROWN': 0.0} )

class HairColorFrequencyMapTestCase5(HairColorFrequencyMapTestCase):
    def runTest(self):
        self.psquare.reduce_by_mothers_traits(['BLOND'])
        self.psquare.reduce_by_fathers_traits(['STRAWBERRY_BLOND'])
        self.assertEqual(self.psquare.get_full_probability_map(), {'STRAWBERRY_BLOND': 0.5, 'BLACK': 0.0, 'BLOND': 0.5, 'RED': 0.0, 'BROWN': 0.0} )

class HairColorFrequencyMapTestCase6(HairColorFrequencyMapTestCase):
    def runTest(self):
        self.psquare.reduce_by_mothers_traits(['BLOND'])
        self.psquare.reduce_by_fathers_traits(['RED'])
        self.assertEqual(self.psquare.get_full_probability_map(), {'STRAWBERRY_BLOND': 1.0, 'BLACK': 0.0, 'BLOND': 0.0, 'RED': 0.0, 'BROWN': 0.0} )


class HairColorFrequencyMapTestCase7(HairColorFrequencyMapTestCase):
    def runTest(self):
        self.psquare.reduce_by_mothers_traits(['STRAWBERRY_BLOND'])
        self.psquare.reduce_by_fathers_traits(['BLACK'])
        self.assertEqual(self.psquare.get_full_probability_map(), {'STRAWBERRY_BLOND': 0.0, 'BLACK': 0.0, 'BLOND': 0.0, 'RED': 0.0, 'BROWN': 1.0} )


class HairColorFrequencyMapTestCase8(HairColorFrequencyMapTestCase):
    def runTest(self):
        self.psquare.reduce_by_mothers_traits(['STRAWBERRY_BLOND'])
        self.psquare.reduce_by_fathers_traits(['RED'])
        self.assertEqual(self.psquare.get_full_probability_map(), {'STRAWBERRY_BLOND': 0.5, 'BLACK': 0.0, 'BLOND': 0.0, 'RED': 0.5, 'BROWN': 0.0} )

class HairColorFrequencyMapTestCase9(HairColorFrequencyMapTestCase):
    def runTest(self):
        self.psquare.reduce_by_mothers_traits(['BLACK'])
        self.psquare.reduce_by_fathers_traits(['RED'])
        self.assertEqual(self.psquare.get_full_probability_map(), {'STRAWBERRY_BLOND': 0.0, 'BLACK': 0.0, 'BLOND': 0.0, 'RED': 0.0, 'BROWN': 1.0} )


class HairColorFrequencyMapTestCase10(HairColorFrequencyMapTestCase):
    def runTest(self):
        self.psquare.reduce_by_mothers_traits(['BLACK'])
        self.psquare.reduce_by_fathers_traits(['BLOND'])
        self.assertEqual(self.psquare.get_full_probability_map(), {'STRAWBERRY_BLOND': 0.0, 'BLACK': 0.0, 'BLOND': 0.0, 'RED': 0.0, 'BROWN': 1.0} )

class HairColorFrequencyMapTestCase11(HairColorFrequencyMapTestCase):
    def runTest(self):
        self.psquare.reduce_by_mothers_traits(['BLACK'])
        self.psquare.reduce_by_fathers_traits(['BROWN'])
        self.assertEqual(self.psquare.get_full_probability_map(), {'STRAWBERRY_BLOND': 0.0, 'BLACK': 0.5, 'BLOND': 0.0, 'RED': 0.0, 'BROWN': 0.5} )


class HairColorFrequencyMapTestCase12(HairColorFrequencyMapTestCase):
    def runTest(self):
        self.psquare.reduce_by_mothers_traits(['RED'])
        self.psquare.reduce_by_fathers_traits(['BROWN'])
        self.assertEqual(self.psquare.get_full_probability_map(), {'STRAWBERRY_BLOND': 0.25, 'BLACK': 0.0, 'BLOND': 0.0, 'RED': 0.25, 'BROWN': 0.5} )


if __name__ == '__main__':
    unittest.main()
