from traits_web_prototype.TraitsEvaluator.TraitsEvaluator import TraitsEvaluator
__author__ = 'yvaskin'


PHENOTYPE_THRESHOLD = 0.2

class PaternityTester:
    def __init__(self,father_traits_map=None, mother_traits_map = None, child_traits_map=None):
        if not father_traits_map: father_traits_map = {}
        if not mother_traits_map: mother_traits_map = {}
        if not child_traits_map: child_traits_map = {}
        self.mother_traits_map = mother_traits_map
        self.father_traits_map = father_traits_map
        self.child_traits_map = child_traits_map
        self.paternity_map = self.__paternity_map()

    def is_father(self):
        return any([val < PHENOTYPE_THRESHOLD for val in self.paternity_map.itervalues()])


    def get_no_proof_traits(self):
        pass

    def get_possible_traits(self):
        pass

    def __paternity_map(self):
        res = {}
        for trait_name in self.child_traits_map.iterkeys():
            res[trait_name] = TraitsEvaluator.phenotype_probability(trait_name, self.father_traits_map.get(trait_name, []), self.mother_traits_map.get(trait_name, []))
        return res