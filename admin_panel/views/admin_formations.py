from django.shortcuts import render
from consult_panel.models import *
from django.contrib.auth.decorators import permission_required
from admin_panel import forms

@permission_required('consult_panel.is_admin')
def formations_index(request):
    context = {
        'page_title'        :   'Gestion des formations',
        'formation_list'    :   Formation.objects.all(),
    }
    return render(request, 'admin_formations_index.html', context=context);

@permission_required('consult_panel.is_admin')
def formations_add(request):
    return render(request, 'admin_formations_add.html', {
        'page_title'        : 'Ajouter une formation',
        'form'              : forms.FormationForm()
    });
    