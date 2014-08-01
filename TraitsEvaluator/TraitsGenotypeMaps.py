__author__ = 'yuriy.vaskin'

class TraitsGenotypeMaps:
    BLOOD_TYPE = dict(
        I=['OO'],
        II=['AO', 'AA'],
        III=['BO', 'BB'],
        IV=['AB'],
    )

    RH_FACTOR = dict(
        PLUS=['RR', 'Rr'],
        MINUS=['rr'],
    )

    EYE_COLOR = dict(
        BROWN=['BB,GG', 'BB,bG', 'BB,bb', 'Bb,GG', 'Bb,bG', 'Bb,bb'],
        GREEN=['bb,GG', 'bb,bG'],
        BLUE=['bb,bb'],
    )

    NAMES = {
        'BLOOD_TYPE': BLOOD_TYPE,
        'RH_FACTOR': RH_FACTOR,
        'EYE_COLOR': EYE_COLOR
    }

