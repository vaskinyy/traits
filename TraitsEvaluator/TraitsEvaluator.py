from TraitsGenotypeMaps import *
import ExtendedPunnettSquare

__author__ = 'yuriy.vaskin'


class TraitsEvaluator:
    def __init__(self):
        pass

    def offspring_frequencies(self, trait, father_traits, mother_traits):
        if trait not in self.get_traits():
            return {}
        traits_map = TraitsGenotypeMaps.NAMES[trait]
        ps = ExtendedPunnettSquare.ExtendedPunnetSquare(traits_map)
        ps.reduce_by_fathers_traits(father_traits)
        ps.reduce_by_mothers_traits(mother_traits)
        return ps.get_traits_frequency_map()

    def get_traits(self):
        return TraitsGenotypeMaps.NAMES.keys()

