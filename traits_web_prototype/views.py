from django.http import HttpResponse
from django.shortcuts import render
from traits_web_prototype.TraitsEvaluator.PaternityTester import PaternityTester
from traits_web_prototype.TraitsEvaluator.TraitsEvaluator import TraitsEvaluator
from traits_web_prototype.models import TraitsForm

def index(request):
    return render(request, 'traits_web_prototype/index.html')

def paternity(request):
    if request.method == 'POST':
        parent_form1 = TraitsForm(request.POST, prefix='parent_form1')
        parent_form2 = TraitsForm(request.POST, prefix='parent_form2')
        child_form = TraitsForm(request.POST, prefix='child_form')
        if parent_form1.is_valid() and parent_form2.is_valid() and child_form.is_valid():
            tester = PaternityTester(parent_form1.get_traits_map(), parent_form2.get_traits_map(), child_form.get_traits_map())

            no_proof = tester.get_no_proof_traits()
            possible = tester.get_possible_traits()
            is_father = tester.is_father()


            #TODO: redirect somewhere
            return render(request, 'traits_web_prototype/paternity.html',
                          {
                              'parent_form1': parent_form1,
                              'parent_form2': parent_form2,
                              'child_form': child_form,
                              'no_proof' : no_proof,
                              'possible' : possible,
                              'is_father' : is_father,
                          })

    else:
            parent_form1 = TraitsForm(prefix='parent_form1')
            parent_form2 = TraitsForm(prefix='parent_form2')
            child_form = TraitsForm(prefix='child_form')


    return render(request, 'traits_web_prototype/paternity.html',
              {
                  'parent_form1': parent_form1,
                  'parent_form2': parent_form2,
                  'child_form': child_form,
              })



def offspring(request):
    if request.method == 'POST':
        parent_form1 = TraitsForm(request.POST, prefix='parent_form1')
        parent_form2 = TraitsForm(request.POST, prefix='parent_form2')
        if parent_form1.is_valid() and parent_form2.is_valid():
            #calculate
            result = []
            teval = TraitsEvaluator()
            for phenotype_name in TraitsEvaluator.get_trait_names():
                result.append(teval.offspring_probs(phenotype_name, [parent_form1.cleaned_data[phenotype_name]], [parent_form2.cleaned_data[phenotype_name]]))

            #TODO: redirect somewhere
            return render(request, 'traits_web_prototype/offspring.html',
                          {
                              'parent_form1': parent_form1,
                              'parent_form2': parent_form2,
                              'result' : result,
                          })

    else:
            parent_form1 = TraitsForm(prefix='parent_form1')
            parent_form2 = TraitsForm(prefix='parent_form2')


    return render(request, 'traits_web_prototype/offspring.html',
              {
                  'parent_form1': parent_form1,
                  'parent_form2': parent_form2,
              })
