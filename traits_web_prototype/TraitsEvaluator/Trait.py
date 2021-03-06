
class Trait:
    def __init__(self, name = None, trait_map=None, phenotype_probs=None):
        if not phenotype_probs: phenotype_probs = dict()
        if not trait_map: trait_map = dict()
        self.trait_map = trait_map
        self.phenotype_probs = phenotype_probs
        self.name = name

    def get_phenotype_probs(self, genotype, phenotype):
        result = 1
        if phenotype in self.phenotype_probs:
           for gt, prob in self.phenotype_probs[phenotype]:
               if gt == genotype:
                    result = prob
                    break

        return result

    def get_phenotypes(self):
        return self.trait_map.keys()
