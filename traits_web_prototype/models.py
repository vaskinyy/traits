from django import forms
from traits_web_prototype.TraitsEvaluator import TraitsGenotypeMaps
from traits_web_prototype.TraitsEvaluator.TraitsEvaluator import TraitsEvaluator


class TraitsForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(TraitsForm, self).__init__(*args, **kwargs)

        for name in TraitsGenotypeMaps.NAMES.keys():
            choices = [(p,p) for p in TraitsEvaluator.get_trait_phenotypes(name)]
            self.fields[name] = forms.ChoiceField(choices=choices)
