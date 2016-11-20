import unittest
from traits_web_prototype.TraitsEvaluator.PaternityTester import PaternityTester
from traits_web_prototype.TraitsEvaluator.TraitsEvaluator import TraitsEvaluator


__author__ = 'yuriy.vaskin'

######################################################
class BasicPaternityTesterCase(unittest.TestCase):
    def setUp(self):
        pass


class BasicPaternityTesterCase1(BasicPaternityTesterCase):
    def runTest(self):
        father_traits_map = {'EYE_COLOR' : ['GREEN']}
        mother_traits_map = {'EYE_COLOR' : ['GREEN']}
        child_traits_map = {'EYE_COLOR' : 'BLUE'}
        tester = PaternityTester(father_traits_map, mother_traits_map, child_traits_map)

        print tester.paternity_map
        print tester.is_parent()
        print tester.get_no_proof_traits()
        print tester.get_possible_traits()


class EyeColorPositiveCase1(BasicPaternityTesterCase):
    def runTest(self):
        father_traits_map = {'EYE_COLOR' : ['BROWN']}
        mother_traits_map = {'EYE_COLOR' : ['BROWN']}
        child_traits_map = {'EYE_COLOR' : 'BLUE'}
        tester = PaternityTester(father_traits_map, mother_traits_map, child_traits_map)

        self.assertTrue(tester.is_parent())


class EyeColorPositiveCase2(BasicPaternityTesterCase):
    def runTest(self):
        father_traits_map = {'EYE_COLOR' : ['GREEN']}
        mother_traits_map = {'EYE_COLOR' : ['BROWN']}
        child_traits_map = {'EYE_COLOR' : ['BROWN']}
        tester = PaternityTester(father_traits_map, mother_traits_map, child_traits_map)

        self.assertTrue(tester.is_parent())


class EyeColorPositiveCase3(BasicPaternityTesterCase):
    def runTest(self):
        father_traits_map = {'EYE_COLOR' : ['GREEN']}
        mother_traits_map = {'EYE_COLOR' : ['GREEN']}
        child_traits_map = {'EYE_COLOR' : ['GREEN']}
        tester = PaternityTester(father_traits_map, mother_traits_map, child_traits_map)

        self.assertTrue(tester.is_parent())

class EyeColorPositiveCase4(BasicPaternityTesterCase):
    def runTest(self):
        father_traits_map = {'EYE_COLOR' : ['BLUE']}
        mother_traits_map = {'EYE_COLOR' : ['BLUE']}
        child_traits_map = {'EYE_COLOR' : ['BLUE']}
        tester = PaternityTester(father_traits_map, mother_traits_map, child_traits_map)

        self.assertTrue(tester.is_parent())


class EyeColorNegativeCase1(BasicPaternityTesterCase):
    def runTest(self):
        father_traits_map = {'EYE_COLOR' : ['BLUE']}
        mother_traits_map = {'EYE_COLOR' : ['BLUE']}
        child_traits_map = {'EYE_COLOR' : ['GREEN']}
        tester = PaternityTester(father_traits_map, mother_traits_map, child_traits_map)

        self.assertFalse(tester.is_parent())
        self.assertIn('EYE_COLOR', tester.get_no_proof_traits())


class EyeColorNegativeCase2(BasicPaternityTesterCase):
    def runTest(self):
        father_traits_map = {'EYE_COLOR' : ['BLUE']}
        mother_traits_map = {'EYE_COLOR' : ['BLUE']}
        child_traits_map = {'EYE_COLOR' : ['BROWN']}
        tester = PaternityTester(father_traits_map, mother_traits_map, child_traits_map)

        self.assertFalse(tester.is_parent())
        self.assertIn('EYE_COLOR', tester.get_no_proof_traits())


class EyeColorNegativeCase3(BasicPaternityTesterCase):
    def runTest(self):
        father_traits_map = {'EYE_COLOR' : ['GREEN']}
        mother_traits_map = {'EYE_COLOR' : ['GREEN']}
        child_traits_map = {'EYE_COLOR' : 'BROWN'}
        tester = PaternityTester(father_traits_map, mother_traits_map, child_traits_map)

        self.assertFalse(tester.is_parent())
        self.assertIn('EYE_COLOR', tester.get_no_proof_traits())


class EyeColorBloodPostiveTest1(BasicPaternityTesterCase):
    def runTest(self):
        father_traits_map = {'EYE_COLOR' : ['GREEN'], 'BLOOD_TYPE' : ['II', 'I']}
        mother_traits_map = {'EYE_COLOR' : ['GREEN', 'BLUE'], 'BLOOD_TYPE' : ['I']}
        child_traits_map = {'EYE_COLOR' : 'GREEN', 'BLOOD_TYPE' : 'I'}
        tester = PaternityTester(father_traits_map, mother_traits_map, child_traits_map)

        self.assertTrue(tester.is_parent())
        self.assertEqual(tester.get_possible_traits(), {'EYE_COLOR': {'BLUE': 0.25, 'GREEN': 0.75}, 'BLOOD_TYPE': {'II': 0.5, 'I': 0.5}})


class EyeColorBloodNegativeTest2(BasicPaternityTesterCase):
    def runTest(self):
        father_traits_map = {'EYE_COLOR' : ['GREEN'], 'BLOOD_TYPE' : ['II', 'I'], 'RH_FACTOR': ['MINUS']}
        mother_traits_map = {'EYE_COLOR' : ['GREEN', 'BLUE'], 'BLOOD_TYPE' : ['III'], 'RH_FACTOR': ['MINUS']}
        child_traits_map = {'EYE_COLOR' : 'GREEN', 'BLOOD_TYPE' : 'I', 'RH_FACTOR': ['PLUS']}
        tester = PaternityTester(father_traits_map, mother_traits_map, child_traits_map)

        self.assertFalse(tester.is_parent())
        self.assertEqual(tester.get_possible_traits(), {'RH_FACTOR': {'MINUS': 1.0}, 'EYE_COLOR': {'BLUE': 0.25, 'GREEN': 0.75}, 'BLOOD_TYPE': {'II': 0.25, 'I': 0.25, 'III': 0.25, 'IV': 0.25}})
        self.assertIn('RH_FACTOR', tester.get_no_proof_traits())


class AllTraitsPositiveTest1(BasicPaternityTesterCase):
    def runTest(self):
        map = {}
        for name in TraitsEvaluator.get_trait_names():
            map[name] = TraitsEvaluator.get_trait_phenotypes(name)[1]
        father_traits_map = map
        mother_traits_map = map
        child_traits_map = map
        tester = PaternityTester(father_traits_map, mother_traits_map, child_traits_map)

        self.assertTrue(tester.is_parent())
        self.assertEqual(tester.get_possible_traits(), {'BITTER_TASTE': {'STRONG_TASTE': 0.8, 'ALMOST_CANT_TASTE': 0.2}, 'ALCOHOL_FLUSH': {'LITTLE_OR_NO': 0.25, 'MODERATE': 0.5, 'EXTREME': 0.25}, 'EARWAX': {'DRY': 0.25, 'WET': 0.75}, 'HAIR_WHORL': {'COUNTER_CLOCKWISE': 0.2175, 'CLOCKWISE': 0.7825}, 'HAIR_COLOR': {'STRAWBERRY_BLOND': 0.125, 'BLACK': 0.25, 'RED': 0.0625, 'BLOND': 0.0625, 'BROWN': 0.5}, 'CLEFT_CHIN': {'CLEFT': 0.2275, 'SMOOTH': 0.7725}, 'EYE_COLOR': {'BLUE': 0.0625, 'BROWN': 0.75, 'GREEN': 0.1875}, 'TONGUE_ROLLING': {'ROLL': 0.835, 'NO_ROLL': 0.165}, 'EARLOBES': {'DISATTACHED': 0.2325, 'ATTACHED': 0.7675}, 'RH_FACTOR': {'PLUS': 0.75, 'MINUS': 0.25}, 'LACTOSE_INTOLERANCE': {'INTOLERANT_LIKELY': 0.25, 'TOLERANT_LIKELY': 0.75}, 'BLOOD_TYPE': {'I': 1.0}})


class AllTraitsNegativeTest1(BasicPaternityTesterCase):
    def runTest(self):
        map = {}
        for name in TraitsEvaluator.get_trait_names():
            map[name] = TraitsEvaluator.get_trait_phenotypes(name)[0]
        father_traits_map = map
        mother_traits_map = map
        child_traits_map = map
        tester = PaternityTester(father_traits_map, mother_traits_map, child_traits_map)

        self.assertFalse(tester.is_parent())
        self.assertEqual(tester.get_possible_traits(), {'BITTER_TASTE': {'STRONG_TASTE': 0.8, 'ALMOST_CANT_TASTE': 0.2}, 'ALCOHOL_FLUSH': {'LITTLE_OR_NO': 0.25, 'MODERATE': 0.5, 'EXTREME': 0.25}, 'EARWAX': {'DRY': 0.25, 'WET': 0.75}, 'HAIR_WHORL': {'COUNTER_CLOCKWISE': 0.2175, 'CLOCKWISE': 0.7825}, 'HAIR_COLOR': {'STRAWBERRY_BLOND': 0.125, 'BLACK': 0.25, 'RED': 0.0625, 'BLOND': 0.0625, 'BROWN': 0.5}, 'CLEFT_CHIN': {'CLEFT': 0.2275, 'SMOOTH': 0.7725}, 'EYE_COLOR': {'BLUE': 0.0625, 'BROWN': 0.75, 'GREEN': 0.1875}, 'TONGUE_ROLLING': {'ROLL': 0.835, 'NO_ROLL': 0.165}, 'EARLOBES': {'DISATTACHED': 0.2325, 'ATTACHED': 0.7675}, 'RH_FACTOR': {'PLUS': 0.75, 'MINUS': 0.25}, 'LACTOSE_INTOLERANCE': {'INTOLERANT_LIKELY': 0.25, 'TOLERANT_LIKELY': 0.75}, 'BLOOD_TYPE': {'I': 1.0}})
        self.assertIn('BLOOD_TYPE', tester.get_no_proof_traits())


class DegenerateCaseUnknownParameter1(BasicPaternityTesterCase):
    def runTest(self):
        father_traits_map1 = {'BLOOD_TYPE' : ['III']}
        mother_traits_map1 = {'BLOOD_TYPE' : ['III', 'II', 'I', 'II']}
        child_traits_map1 = {'BLOOD_TYPE' : 'III'}
        tester1 = PaternityTester(father_traits_map1, mother_traits_map1, child_traits_map1)


        father_traits_map = {'BLOOD_TYPE' : ['III']}
        mother_traits_map = {'BLOOD_TYPE' : ['unknown']}
        child_traits_map = {'BLOOD_TYPE' : 'III'}
        tester = PaternityTester(father_traits_map, mother_traits_map, child_traits_map)

        self.assertEqual(tester.get_possible_traits(), tester1.get_possible_traits())


class DegenerateCaseUnknownParameter2(BasicPaternityTesterCase):
    def runTest(self):
        father_traits_map1 = {'BLOOD_TYPE' : ['III', 'II', 'I', 'II']}
        mother_traits_map1 = {'BLOOD_TYPE' : ['III']}
        child_traits_map1 = {'BLOOD_TYPE' : 'III'}
        tester1 = PaternityTester(father_traits_map1, mother_traits_map1, child_traits_map1)


        father_traits_map = {'BLOOD_TYPE' : ['unknown']}
        mother_traits_map = {'BLOOD_TYPE' : ['III']}
        child_traits_map = {'BLOOD_TYPE' : 'III'}
        tester = PaternityTester(father_traits_map, mother_traits_map, child_traits_map)

        self.assertEqual(tester.get_possible_traits(), tester1.get_possible_traits())


class DegenerateCaseUnknownParameter3(BasicPaternityTesterCase):
    def runTest(self):
        father_traits_map1 = {'BLOOD_TYPE' : ['I']}
        mother_traits_map1 = {'BLOOD_TYPE' : ['II']}
        child_traits_map1 = {'BLOOD_TYPE' : 'II'}
        tester1 = PaternityTester(father_traits_map1, mother_traits_map1, child_traits_map1)


        father_traits_map = {'BLOOD_TYPE' : ['unknown']}
        mother_traits_map = {'BLOOD_TYPE' : ['II']}
        child_traits_map = {'BLOOD_TYPE' : 'II'}
        tester = PaternityTester(father_traits_map, mother_traits_map, child_traits_map)

        self.assertNotEqual(tester.get_possible_traits(), tester1.get_possible_traits())


class DegenerateCaseUnknownParameter4(BasicPaternityTesterCase):
    def runTest(self):
        father_traits_map1 = {'BLOOD_TYPE' : ['II']}
        mother_traits_map1 = {'BLOOD_TYPE' : ['II']}
        child_traits_map1 = {'BLOOD_TYPE' : ['I', 'II', 'III', 'IV']}
        tester1 = PaternityTester(father_traits_map1, mother_traits_map1, child_traits_map1)


        father_traits_map = {'BLOOD_TYPE' : ['II']}
        mother_traits_map = {'BLOOD_TYPE' : ['II']}
        child_traits_map = {'BLOOD_TYPE' : 'unknown'}
        tester = PaternityTester(father_traits_map, mother_traits_map, child_traits_map)

        self.assertEqual(tester.get_possible_traits(), tester1.get_possible_traits())


class DegenerateCaseOddParameter5(BasicPaternityTesterCase):
    def runTest(self):
        father_traits_map1 = {'BLOOD_TYPE' : ['II']}
        mother_traits_map1 = {'BLOOD_TYPE' : ['II']}
        child_traits_map1 = {'BLOOD_TYPE' : ['II', 'asdfdsf']}
        tester1 = PaternityTester(father_traits_map1, mother_traits_map1, child_traits_map1)


        father_traits_map = {'BLOOD_TYPE' : ['II']}
        mother_traits_map = {'BLOOD_TYPE' : ['II']}
        child_traits_map = {'BLOOD_TYPE' : 'II'}
        tester = PaternityTester(father_traits_map, mother_traits_map, child_traits_map)

        self.assertEqual(tester.get_possible_traits(), tester1.get_possible_traits())


class DegenerateCaseEmptyParameter6(BasicPaternityTesterCase):
    def runTest(self):
        father_traits_map1 = {'BLOOD_TYPE' : []}
        mother_traits_map1 = {'BLOOD_TYPE' : ['II']}
        child_traits_map1 = {'BLOOD_TYPE' : ['II']}
        tester1 = PaternityTester(father_traits_map1, mother_traits_map1, child_traits_map1)


        father_traits_map = {'BLOOD_TYPE' : ['II', 'I', 'IV', 'III']}
        mother_traits_map = {'BLOOD_TYPE' : ['II']}
        child_traits_map = {'BLOOD_TYPE' : 'II'}
        tester = PaternityTester(father_traits_map, mother_traits_map, child_traits_map)

        self.assertEqual(tester.get_possible_traits(), tester1.get_possible_traits())


class DegenerateCaseEmptyParameter7(BasicPaternityTesterCase):
    def runTest(self):
        mother_traits_map1 = {'BLOOD_TYPE' : ['II']}
        child_traits_map1 = {'BLOOD_TYPE' : ['II']}
        tester1 = PaternityTester(None, mother_traits_map1, child_traits_map1)


        father_traits_map = {'BLOOD_TYPE' : ['II', 'I', 'IV', 'III']}
        mother_traits_map = {'BLOOD_TYPE' : ['II']}
        child_traits_map = {'BLOOD_TYPE' : 'II'}
        tester = PaternityTester(father_traits_map, mother_traits_map, child_traits_map)

        self.assertEqual(tester.get_possible_traits(), tester1.get_possible_traits())


class DegenerateCaseEmptyParameter8(BasicPaternityTesterCase):
    def runTest(self):
        father_traits_map1 = {'BLOOD_TYPE' : ['II']}
        mother_traits_map1 = {'BLOOD_TYPE' : ['II']}
        child_traits_map1 = {'BLOOD_TYPE' : []}
        tester1 = PaternityTester(father_traits_map1, mother_traits_map1, child_traits_map1)


        father_traits_map = {'BLOOD_TYPE' : ['II']}
        mother_traits_map = {'BLOOD_TYPE' : ['II']}
        child_traits_map = {'BLOOD_TYPE' : ['II', 'I', 'IV', 'III']}
        tester = PaternityTester(father_traits_map, mother_traits_map, child_traits_map)

        self.assertEqual(tester.get_possible_traits(), tester1.get_possible_traits())


class DegenerateCaseNoParameter9(BasicPaternityTesterCase):
    def runTest(self):
        father_traits_map1 = {'EYE_COLOR' : ['GREEN'], 'BLOOD_TYPE' : ['II', 'I', 'II', 'III']}
        mother_traits_map1 = {'EYE_COLOR' : ['GREEN', 'BLUE'], 'BLOOD_TYPE' : ['II', 'I', 'II', 'III']}
        child_traits_map1 = {'EYE_COLOR' : 'GREEN', 'BLOOD_TYPE' : 'I'}
        tester1 = PaternityTester(father_traits_map1, mother_traits_map1,child_traits_map1)


        father_traits_map = {'EYE_COLOR' : ['GREEN']}
        mother_traits_map = {'EYE_COLOR' : ['GREEN', 'BLUE']}
        child_traits_map = {'EYE_COLOR' : 'GREEN', 'BLOOD_TYPE' : 'I'}
        tester = PaternityTester(father_traits_map, mother_traits_map, child_traits_map)

        self.assertEqual(tester.get_possible_traits(), tester1.get_possible_traits())


class DegenerateCaseNoParameter10(BasicPaternityTesterCase):
    def runTest(self):
        father_traits_map1 = {'EYE_COLOR' : ['GREEN'], 'BLOOD_TYPE' : ['II']}
        mother_traits_map1 = {'EYE_COLOR' : ['GREEN', 'BLUE'], 'BLOOD_TYPE' : ['II']}
        child_traits_map1 = {'EYE_COLOR' : 'GREEN'}
        tester1 = PaternityTester(father_traits_map1, mother_traits_map1,child_traits_map1)


        father_traits_map = {'EYE_COLOR' : ['GREEN']}
        mother_traits_map = {'EYE_COLOR' : ['GREEN', 'BLUE']}
        child_traits_map = {'EYE_COLOR' : 'GREEN'}
        tester = PaternityTester(father_traits_map, mother_traits_map, child_traits_map)

        self.assertEqual(tester.get_possible_traits(), tester1.get_possible_traits())


######################################################

class StatisticsPaternityTester(unittest.TestCase):
    def setUp(self):
        pass
