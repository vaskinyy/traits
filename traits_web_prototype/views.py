from django.http import HttpResponse
from django.shortcuts import render
from traits_web_prototype.TraitsEvaluator.TraitsEvaluator import TraitsEvaluator
from traits_web_prototype.models import TraitsForm

def index_(request):
    return HttpResponse('Yo')

def index(request):
    if request.method == 'POST':
        print request.POST
        parent_form1 = TraitsForm(request.POST, prefix='parent_form1')
        parent_form2 = TraitsForm(request.POST, prefix='parent_form2')
        if parent_form1.is_valid() and parent_form2.is_valid():
            #calculate
            result = []
            print parent_form1.cleaned_data
            teval = TraitsEvaluator()
            result.append(teval.offspring_frequencies('EYE_COLOR', [parent_form1.cleaned_data['eye_color']], [parent_form2.cleaned_data['eye_color']]))
            result.append(teval.offspring_frequencies('BLOOD_TYPE', [parent_form1.cleaned_data['blood_type']], [parent_form2.cleaned_data['blood_type']]))
            result.append(teval.offspring_frequencies('RH_FACTOR', [parent_form1.cleaned_data['rh_type']], [parent_form2.cleaned_data['rh_type']]))
            print result

            #TODO: redirect somewhere
            return render(request, 'traits_web_prototype/index.html',
                          {
                              'parent_form1': parent_form1,
                              'parent_form2': parent_form2,
                              'result' : result,
                          })
    else:
            parent_form1 = TraitsForm(prefix='parent_form1')
            parent_form2 = TraitsForm(prefix='parent_form2')


    return render(request, 'traits_web_prototype/index.html',
              {
                  'parent_form1': parent_form1,
                  'parent_form2': parent_form2,
              })
