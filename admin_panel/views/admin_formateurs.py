from django.shortcuts import render
from consult_panel.models import *
from django.contrib.auth.decorators import permission_required
from admin_panel import forms

def formateurs_index(request):
    return render(request, 'admin_formateurs_index.html', context={
                  'page_title'          :   'Gestion des formateurs',
                  'profiles_list'       : Profile.objects.all()
                  });

def formateurs_add(request):
    return render(request, 'admin_formateurs_add.html', {
                  'page_title'        : 'Ajouter une formation',
                  'form'              : forms.ProfileForm()
                  });
    
def formateurs_edit(request, id):
    return render(request, 'admin_formateurs_edit.html', {
                  'page_title'        : 'Editer une formation',
                  'form'              : forms.ProfileForm(instance=Profile.objects.get(pk=id))
                  });
    