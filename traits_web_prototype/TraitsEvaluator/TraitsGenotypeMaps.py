from traits_web_prototype.TraitsEvaluator.Trait import *

#http://udel.edu/~mcdonald/mythearlobe.html
#https://www.23andme.com/you/inheritance/
#http://dna.frieger.com/calc-quick.php

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


HAIR_COLOR_MAP = dict(
    BLACK = ['BB,NN', 'BB,Nn', 'BB,nn'],
    BROWN = ['Bb,NN', 'Bb,Nn', 'Bb,nn'],
    STRAWBERRY_BLOND = ['bb,Nn'],
    BLOND = ['bb,NN'],
    RED = ['bb,nn'],
)


LACTOSE_INTOLERANCE_MAP = dict(
    TOLERANT_LIKELY=['AA', 'AG'],
    INTOLERANT_LIKELY=['GG'],
)

EARWAX_MAP = dict(
    WET=['CC', 'CT'],
    DRY=['TT'],
)

ALCOHOL_FLUSH_MAP = dict(
    EXTREME=['AA'],
    MODERATE=['AG'],
    LITTLE_OR_NO=['GG'],
)

BITTER_TASTE_MAP = dict(
    STRONG_TASTE=['CG', 'CC', 'GG'],
    ALMOST_CANT_TASTE=['CC'],
)
BITTER_TASTE_PROBS = dict(
    STRONG_TASTE=[('CC', 0.2)],
    ALMOST_CANT_TASTE=[('CC', 0.8)],
)

EARLOBES_MAP = dict(
    ATTACHED=['AA', 'Ad', 'dd'],
    DISATTACHED=['dd'],
)
EARLOBES_PROBS = dict(
    ATTACHED=[('dd', 0.07)],
    DISATTACHED=[('dd', 0.93)],
)

CLEFT_CHIN_MAP = dict(
    SMOOTH=['SS', 'cS', 'cc'],
    CLEFT=['cc'],
)
CLEFT_CHIN_PROBS = dict(
    SMOOTH=[('cc', 0.09)],
    CLEFT=[('cc', 0.91)],
)

HAIR_WHORL_MAP = dict(
    CLOCKWISE=['RR', 'Rr', 'rr'],
    COUNTER_CLOCKWISE=['rr'],

)
HAIR_WHORL_PROBS = dict(
    CLOCKWISE=[('rr', 0.13)],
    COUNTER_CLOCKWISE=[('rr', 0.87)],
)

TONGUE_ROLLING_MAP = dict(
    ROLL=['RR', 'nR', 'nn'],
    NO_ROLL=['nn'],
)
TONGUE_ROLLING_PROBS = dict(
    ROLL=[('nn', 0.34)],
    NO_ROLL=[('nn', 0.66)],
)


NAMES = {
    'BLOOD_TYPE': (BLOOD_TYPE_MAP, None),
    'RH_FACTOR': (RH_FACTOR_MAP, None),
    'EYE_COLOR': (EYE_COLOR_MAP, None),
    #'HAIR_COLOR': (HAIR_COLOR_MAP, None),
    #'LACTOSE_INTOLERANCE': (LACTOSE_INTOLERANCE_MAP, None),
    #'EARWAX': (EARWAX_MAP, None),
    #'ALCOHOL_FLUSH': (ALCOHOL_FLUSH_MAP, None),
    #'BITTER_TASTE': (BITTER_TASTE_MAP, BITTER_TASTE_PROBS),
    #'EARLOBES': (EARLOBES_MAP, EARLOBES_PROBS),
    #'CLEFT_CHIN': (CLEFT_CHIN_MAP, CLEFT_CHIN_PROBS),
    #'HAIR_WHORL': (HAIR_WHORL_MAP, HAIR_WHORL_PROBS),
    #'TONGUE_ROLLING': (TONGUE_ROLLING_MAP, TONGUE_ROLLING_PROBS),
}

