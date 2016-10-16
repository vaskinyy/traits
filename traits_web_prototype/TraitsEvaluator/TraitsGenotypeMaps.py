from traits_web_prototype.TraitsEvaluator.Trait import *

BLOOD_TYPE_MAP = dict(
    I=['OO'],
    II=['AO', 'AA'],
    III=['BO', 'BB'],
    IV=['AB'],
)

RH_FACTOR_MAP = dict(
    PLUS=['RR', 'Rr'],
    MINUS=['rr'],
)

EYE_COLOR_MAP = dict(
    BROWN=['BB,GG', 'BB,bG', 'BB,bb', 'Bb,GG', 'Bb,bG', 'Bb,bb'],
    GREEN=['bb,GG', 'bb,bG'],
    BLUE=['bb,bb'],
)

NAMES = {
        'BLOOD_TYPE': (BLOOD_TYPE_MAP, None),
        'RH_FACTOR': (RH_FACTOR_MAP, None),
        'EYE_COLOR': (EYE_COLOR_MAP, None)
    }


"""
WIDOWS_PEAK = dict(
    PEAK=['RR', 'Rr'],
    NO_PEAK=['rr'],
)

EARLOBES = dict(
    DISATTACHED=['RR', 'Rr'],
    ATTACHED=['rr', 'Rr'],
)

CLEFT_CHIN = dict(
    CLEFT=['RR', 'Rr'],
    SMOOTH=['rr', 'Rr'],
)

HAIR_WHORL = dict(
    CLOCKWISE=['RR', 'Rr'],
    COUNTER_CLOCKWISE=['rr'],
)

BITTER_TASTE = dict(
    STRONG_TASTE=['RR', 'Rr'],
    ALMOST_CANT_TASTE=['rr'],
)

TONGUE_ROLLING = dict(
    ROLL=['RR', 'Rr'],
    NO_ROLL=['rr', 'Rr'],
)
"""


