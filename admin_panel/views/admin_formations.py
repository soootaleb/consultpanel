from django.shortcuts import render
from consult_panel.models import *
from admin_panel.forms import forms

def formations_index(request):
    return render(request, 'admin_formations_index.html', context={
                  'page_title'        :   'Gestion des formations',
                  'formations_list'   :   Formation.objects.all(),
                  });

def formations_add(request):
    return render(request, 'admin_formations_add.html', {
                  'page_title'        : 'Ajouter une formation',
                  'form'              : forms.FormationForm()
                  });
    
def formations_edit(request, id):
    return render(request, 'admin_formations_edit.html', {
                  'page_title'        : 'Editer une formation',
                  'form'              : forms.FormationForm(instance=Formation.objects.get(pk=id))
                  });
    