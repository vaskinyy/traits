from collections import OrderedDict
import unittest
from traits_web_prototype.TraitsEvaluator.PaternityTester import PaternityTester
from traits_web_prototype.TraitsEvaluator.TraitsEvaluator import TraitsEvaluator
import time


__author__ = 'yuriy.vaskin'

class TraitsCombinations:
    def __init__(self, with_unknown = False, trait_names=None):
        self.trait_names = TraitsEvaluator.get_trait_names()
        if trait_names is not None:
            self.trait_names = trait_names

        self.with_unknown = with_unknown

        self.lenghts = self.__get_lenghts()
        self.index = [0] * len(self.lenghts)
        self.first = True

    def number_of_combinations(self):
        return reduce( (lambda x, y: x * y), self.lenghts )

    def has_next(self):
        return any([self.__can_increase(i) for i in range(0, len(self.index))])

    def next(self):
        if self.first:
            self.first = False
            return
        for i in range(0,len(self.index)):
            if self.__can_increase(i):
                self.index[i] += 1
                break
            elif self.index[i] + 1 == self.lenghts[i]:
                for j in range(0, i+1):
                    self.index[i] = 0
        return


    def __can_increase(self, idx):
        return self.index[idx] + 1 < self.lenghts[idx]


    def __get_lenghts(self):
        res = []
        for i in range(0,3):
            for trait_name in self.trait_names:
                number = len(TraitsEvaluator.get_trait_phenotypes(trait_name))
                if self.with_unknown and i != 2:
                    number += 1
                res.append(number)
        return res

    def get_father_traits(self):
        return self.__get_traits(self.__get_father_index())

    def get_mother_traits(self):
        return self.__get_traits(self.__get_mother_index())

    def get_child_traits(self):
        return self.__get_traits(self.__get_child_index())

    def __get_traits(self, index):
        res = {}
        for i in range(0, len(self.trait_names)):
            phenotypes = TraitsEvaluator.get_trait_phenotypes(self.trait_names[i])

            if len(phenotypes) == index[i]:
                res[self.trait_names[i]] = phenotypes
            else:
                res[self.trait_names[i]] = [ phenotypes[index[i]] ]
        return res


    def __get_father_index(self):
        trait_len = len(self.trait_names)
        return self.index[0:trait_len]

    def __get_mother_index(self):
        trait_len = len(self.trait_names)
        return self.index[trait_len : trait_len*2]

    def __get_child_index(self):
        trait_len = len(self.trait_names)
        return self.index[trait_len*2 : ]


#####################################################
class StatisticsPaternityTester(unittest.TestCase):
    def setUp(self):
        pass


# class IsFatherCounter(StatisticsPaternityTester):
#     def update_not_father_traits(self, current_no_proofs):
#         for trait_name in current_no_proofs.keys():
#             if trait_name not in self.not_father_traits:
#                 self.not_father_traits[trait_name] = 0
#             self.not_father_traits[trait_name] += 1
#
#     def setUp(self):
#         self.combinator = TraitsCombinations()
#         self.not_father_traits = {}
#
#     def runTest(self):
#         print "number of iterations %s" % self.combinator.number_of_combinations()
#         not_father_counter = 0
#         iter_counter = 0
#
#         start = time.time()
#         while self.combinator.has_next():
#             iter_counter+=1
#             if iter_counter % 10000 == 0:
#                 print iter_counter / float(time.time() - start)
#
#             self.combinator.next()
#             tester = PaternityTester(self.combinator.get_father_traits(), self.combinator.get_mother_traits(), self.combinator.get_child_traits())
#             if not tester.is_parent():
#                 not_father_counter += 1
#                 self.update_not_father_traits(tester.get_no_proof_traits())
#
#         print "number of iterations %s" % self.combinator.number_of_combinations()
#         print 'not father %s' % not_father_counter
#         print self.not_father_traits
#

class TraitIsFatherPowerTesterCounter(StatisticsPaternityTester):
    def runTest(self):
        powers = {}

        for trait_name in TraitsEvaluator.get_trait_names():
            not_father_counter = 0
            #combinator = TraitsCombinations(with_unknown=True, trait_names=[trait_name])
            combinator = TraitsCombinations(trait_names=[trait_name])

            while combinator.has_next():
                combinator.next()
                tester = PaternityTester(combinator.get_father_traits(), combinator.get_mother_traits(), combinator.get_child_traits())
                if not tester.is_parent():
                    not_father_counter += 1
            powers[trait_name] = not_father_counter / float(combinator.number_of_combinations())

        print OrderedDict(sorted(powers.items(), key=lambda t: t[1], reverse=True))

        #0.05
        #OrderedDict([('HAIR_COLOR', 0.592), ('ALCOHOL_FLUSH', 0.4444444444444444), ('BLOOD_TYPE', 0.375), ('EYE_COLOR', 0.18518518518518517), ('CURLY_HAIR', 0.125), ('HITCHHIKERS_THUMBS', 0.125), ('EARWAX', 0.125), ('RH_FACTOR', 0.125), ('LACTOSE_INTOLERANCE', 0.125), ('BITTER_TASTE', 0.0), ('CLEFT_CHIN', 0.0), ('HAIR_WHORL', 0.0), ('TONGUE_ROLLING', 0.0), ('EARLOBES', 0.0)])

        #0.21
        #OrderedDict([('HAIR_COLOR', 0.648), ('ALCOHOL_FLUSH', 0.4444444444444444), ('BLOOD_TYPE', 0.375), ('EYE_COLOR', 0.3333333333333333), ('BITTER_TASTE', 0.25), ('CURLY_HAIR', 0.125), ('HITCHHIKERS_THUMBS', 0.125), ('EARWAX', 0.125), ('CLEFT_CHIN', 0.125), ('HAIR_WHORL', 0.125), ('TONGUE_ROLLING', 0.125), ('EARLOBES', 0.125), ('RH_FACTOR', 0.125), ('LACTOSE_INTOLERANCE', 0.125)])

        ###with unknown
        #0.05
        #OrderedDict([('HAIR_COLOR', 0.5), ('ALCOHOL_FLUSH', 0.3333333333333333), ('BLOOD_TYPE', 0.28), ('EYE_COLOR', 0.10416666666666667), ('CURLY_HAIR', 0.05555555555555555), ('HITCHHIKERS_THUMBS', 0.05555555555555555), ('EARWAX', 0.05555555555555555), ('RH_FACTOR', 0.05555555555555555), ('LACTOSE_INTOLERANCE', 0.05555555555555555), ('BITTER_TASTE', 0.0), ('CLEFT_CHIN', 0.0), ('HAIR_WHORL', 0.0), ('TONGUE_ROLLING', 0.0), ('EARLOBES', 0.0)])

        #0.21
        #OrderedDict([('HAIR_COLOR', 0.6111111111111112), ('BLOOD_TYPE', 0.41), ('EYE_COLOR', 0.3541666666666667), ('ALCOHOL_FLUSH', 0.3333333333333333), ('BITTER_TASTE', 0.2777777777777778), ('TONGUE_ROLLING', 0.2222222222222222), ('CURLY_HAIR', 0.05555555555555555), ('HITCHHIKERS_THUMBS', 0.05555555555555555), ('EARWAX', 0.05555555555555555), ('CLEFT_CHIN', 0.05555555555555555), ('HAIR_WHORL', 0.05555555555555555), ('EARLOBES', 0.05555555555555555), ('RH_FACTOR', 0.05555555555555555), ('LACTOSE_INTOLERANCE', 0.05555555555555555)])


