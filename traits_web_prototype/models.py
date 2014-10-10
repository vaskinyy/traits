from django.db import models
from django import forms


class TraitsForm(forms.Form):
    EYE_COLOR = (
        ('BROWN', 'BROWN'),
        ('GREEN', 'GREEN'),
        ('BLUE', 'BLUE'),
    )
    eye_color = forms.ChoiceField(choices=EYE_COLOR)

    BLOOD_TYPE = (
        ('I', 'I'),
        ('II', 'II'),
        ('III', 'III'),
        ('IV', 'IV'),
    )
    blood_type = forms.ChoiceField(choices=BLOOD_TYPE)

    RH_TYPE = (
        ('+', '+'),
        ('-', '-'),
    )
    rh_type = forms.ChoiceField(choices=RH_TYPE)
