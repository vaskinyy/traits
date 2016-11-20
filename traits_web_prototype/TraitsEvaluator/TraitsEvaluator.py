from TraitsGenotypeMaps import *
import ExtendedPunnettSquare

__author__ = 'yuriy.vaskin'


class TraitsEvaluator:
    @staticmethod
    def offspring_probs(trait_name, father_traits, mother_traits):
        trait = TraitsEvaluator.get_trait(trait_name)
        ps = ExtendedPunnettSquare.ExtendedPunnetSquare(trait)
        ps.reduce_by_fathers_traits(father_traits)
        ps.reduce_by_mothers_traits(mother_traits)
        return ps.get_full_probability_map()

    @staticmethod
    def phenotype_probability(trait_name, father_traits, mother_traits, phenotype):
        trait = TraitsEvaluator.get_trait(trait_name)
        ps = ExtendedPunnettSquare.ExtendedPunnetSquare(trait)
        ps.reduce_by_fathers_traits(father_traits)
        ps.reduce_by_mothers_traits(mother_traits)
        return ps.get_phenotype_probability(phenotype)

    @staticmethod
    def offspring_traits(trait_name, father_traits, mother_traits):
        res = []
        prob_map = TraitsEvaluator.offspring_probs(trait_name, father_traits, mother_traits)
        for trait in prob_map.keys():
            if prob_map[trait] != 0:
                res.append(trait)
        return res


    #TODO warning: do not use for a general case
    @staticmethod
    def reduce_traits(trait_name, father_traits, mother_traits, child_traits):
        if father_traits == []: father_traits = TraitsEvaluator.get_trait_phenotypes(trait_name)
        if mother_traits == []: mother_traits = TraitsEvaluator.get_trait_phenotypes(trait_name)
        if child_traits == []: child_traits = TraitsEvaluator.get_trait_phenotypes(trait_name)
        possible_offspring_traits = TraitsEvaluator.offspring_traits(trait_name, father_traits, mother_traits)
        res = [t for t in child_traits if t in possible_offspring_traits]
        return res


    @staticmethod
    def get_trait_names():
        return NAMES.keys()

    @staticmethod
    def get_trait(name):
        if name in NAMES:
            map, probs = NAMES[name]
            return Trait(name, map, probs)
        return Trait()

    @staticmethod
    def get_trait_phenotypes(name):
        trait = TraitsEvaluator.get_trait(name)
        return trait.trait_map.keys()
