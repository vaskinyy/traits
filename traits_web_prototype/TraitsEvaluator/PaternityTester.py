from traits_web_prototype.TraitsEvaluator.TraitsEvaluator import TraitsEvaluator
__author__ = 'yvaskin'


PHENOTYPE_THRESHOLD = 0.05

class PaternityTester:
    def __init__(self,father_traits_map=None, mother_traits_map = None, child_traits_map=None):
        if not father_traits_map: father_traits_map = {}
        if not mother_traits_map: mother_traits_map = {}
        if not child_traits_map: child_traits_map = {}

        self.father_traits_map = father_traits_map
        self.mother_traits_map = mother_traits_map
        self.child_traits_map = self.__reformat_child_map(child_traits_map)

        self.paternity_map = self.__paternity_map()


    def is_parent(self):
        return all([self.__is_passes_test(val) for val in self.paternity_map.itervalues()])


    def get_no_proof_traits(self):
        res = {}
        offspring_traits = self.__get_offspring_traits()
        for trait_name in offspring_traits:
            dict = {t:p for (t,p) in offspring_traits[trait_name].items() if not self.__is_passes_test(p) and t == self.child_traits_map[trait_name]}
            if len(dict) != 0:
                res[trait_name] = dict
        return res



    def get_possible_traits(self):
        res = {}
        offspring_traits = self.__get_offspring_traits()
        for trait_name in offspring_traits:
            res[trait_name] = {t:p for (t,p) in offspring_traits[trait_name].items() if self.__is_passes_test(p)}
        return res



    def __paternity_map(self):
        res = {}
        for trait_name in self.child_traits_map.iterkeys():
            res[trait_name] = TraitsEvaluator.phenotype_probability(trait_name, self.father_traits_map.get(trait_name, []), self.mother_traits_map.get(trait_name, []), self.child_traits_map[trait_name])
        return res


    def __is_passes_test(self, val):
        return val >= PHENOTYPE_THRESHOLD

    def __get_offspring_traits(self):
        res = {}
        for trait_name in self.paternity_map.iterkeys():
            probs = TraitsEvaluator.offspring_probs(trait_name, self.father_traits_map.get(trait_name, []), self.mother_traits_map.get(trait_name, []))
            res[trait_name] = probs
        return res


    def __reformat_child_map(self, child_map):
        res = {}
        for name in child_map.keys():
            if isinstance(child_map[name], list):
                if len(child_map[name]) == 0:
                    res[name] = ''
                else:
                    res[name] = child_map[name][0]
            else:
                res[name] = child_map[name]
        return res
