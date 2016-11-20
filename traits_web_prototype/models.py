from django import forms
from traits_web_prototype.TraitsEvaluator import TraitsGenotypeMaps
from traits_web_prototype.TraitsEvaluator.TraitsEvaluator import TraitsEvaluator


class TraitsForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(TraitsForm, self).__init__(*args, **kwargs)

        for name in TraitsEvaluator.get_trait_names():
            choices = [(p,p) for p in TraitsEvaluator.get_trait_phenotypes(name)]
            choices.append(('unknown', 'unknown'))
            self.fields[name] = forms.ChoiceField(choices=choices)


    def get_traits_map(self):
        res = {}
        for name in TraitsEvaluator.get_trait_names():
            res[name] = [self.cleaned_data[name]]
        return res

