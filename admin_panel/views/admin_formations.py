from django.shortcuts import render
from consult_panel.models import *
from django.contrib.auth.decorators import permission_required
from admin_panel import forms

@permission_required('consult_panel.is_admin')
def formations_index(request):
    return render(request, 'admin_formations_index.html', context={
        'page_title'        :   'Gestion des formations',
        'formation_list'    :   Formation.objects.all(),
    });

@permission_required('consult_panel.is_admin')
def formations_add(request):
    return render(request, 'admin_formations_add.html', {
        'page_title'        : 'Ajouter une formation',
        'form'              : forms.FormationForm()
    });
    
@permission_required('consult_panel.is_admin')
def formations_edit(request, id):
    return render(request, 'admin_formations_edit.html', {
        'page_title'        : 'Editer une formation',
        'form'              : forms.FormationForm(instance=Formation.objects.get(pk=id))
    });
    