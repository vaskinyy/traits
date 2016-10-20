from TraitsGenotypeMaps import *
import ExtendedPunnettSquare

__author__ = 'yuriy.vaskin'


class TraitsEvaluator:
    def __init__(self):
        pass

    def offspring_frequencies(self, trait_name, father_traits, mother_traits):
        trait = TraitsEvaluator.get_trait(trait_name)
        ps = ExtendedPunnettSquare.ExtendedPunnetSquare(trait)
        ps.reduce_by_fathers_traits(father_traits)
        ps.reduce_by_mothers_traits(mother_traits)
        return ps.get_traits_probability_map()

    @staticmethod
    def get_trait_names():
        return NAMES.keys()

    @staticmethod
    def get_trait(name):
        if name in NAMES:
            map, probs = NAMES[name]
            return Trait(map, probs)
        return Trait()

    @staticmethod
    def get_trait_phenotypes(name):
        trait = TraitsEvaluator.get_trait(name)
        return trait.trait_map.keys()
