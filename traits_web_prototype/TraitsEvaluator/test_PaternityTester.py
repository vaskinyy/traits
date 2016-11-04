import unittest
from traits_web_prototype.TraitsEvaluator.PaternityTester import PaternityTester


__author__ = 'yuriy.vaskin'

######################################################
class BasicPaternityTesterCase(unittest.TestCase):
    def setUp(self):
        pass


class BasicPaternityTesterCase1(BasicPaternityTesterCase):
    def runTest(self):
        father_traits_map = {'EYE_COLOR' : ['BLUE']}
        mother_traits_map = {'EYE_COLOR' : ['BROWN']}
        child_traits_map = {'EYE_COLOR' : 'GREEN'}
        tester = PaternityTester(father_traits_map, mother_traits_map, child_traits_map)

        print tester.paternity_map
        print tester.is_father()
        print tester.get_no_proof_traits()
        print tester.get_possible_traits()


######################################################

class StatisticsPaternityTester(unittest.TestCase):
    def setUp(self):
        pass
