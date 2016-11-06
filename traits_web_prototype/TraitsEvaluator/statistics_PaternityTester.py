import unittest
from traits_web_prototype.TraitsEvaluator.PaternityTester import PaternityTester
from traits_web_prototype.TraitsEvaluator.TraitsEvaluator import TraitsEvaluator


__author__ = 'yuriy.vaskin'

#TODO finish me
class TraitsCombinations:
    def __init__(self, with_unknown = False):
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
        trait_names = TraitsEvaluator.get_trait_names()
        for i in range(0,3):
            for trait_name in trait_names:
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
        trait_names = TraitsEvaluator.get_trait_names()
        for i in range(0, len(trait_names)):
            phenotypes = TraitsEvaluator.get_trait_phenotypes(trait_names[i])

            if len(phenotypes) == index[i]:
                res[trait_names[i]] = phenotypes
            else:
                res[trait_names[i]] = [ phenotypes[index[i]] ]
        return res


    def __get_father_index(self):
        trait_len = len(TraitsEvaluator.get_trait_names())
        return self.index[0:trait_len]

    def __get_mother_index(self):
        trait_len = len(TraitsEvaluator.get_trait_names())
        return self.index[trait_len : trait_len*2]

    def __get_child_index(self):
        trait_len = len(TraitsEvaluator.get_trait_names())
        return self.index[trait_len*2 : ]


#####################################################
class StatisticsPaternityTester(unittest.TestCase):
    def setUp(self):
        pass


class IsFatherCounter(StatisticsPaternityTester):
    def runTest(self):
        combinator = TraitsCombinations()
        #print combinator.lenghts
        iteration_counter = 0
        not_father_counter = 0
        while combinator.has_next():
            combinator.next()
            tester = PaternityTester(combinator.get_father_traits(), combinator.get_mother_traits(), combinator.get_child_traits())
            if not tester.is_father():
                not_father_counter += 1
            iteration_counter += 1
            #print combinator.lenghts
        print 'iterations %s' % iteration_counter
        print 'not father %s' % not_father_counter
