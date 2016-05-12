from django.shortcuts import render
from consult_panel.models import *
from django.contrib.auth.decorators import permission_required
from admin_panel.forms import forms

def catalogues_index(request):
    return render(request, 'admin_catalogues_index.html', context={
        'page_title'        :   'Gestion des catalogues',
        'catalogues_list'    :   Catalogue.objects.all(),
    });

def catalogues_add(request):
    return render(request, 'admin_catalogues_add.html', {
        'page_title'        : 'Ajouter un catalogue',
        'form'              : forms.CatalogueForm()
    });
    
def catalogues_edit(request, id):
    return render(request, 'admin_catalogues_edit.html', {
        'page_title'        : 'Editer un catalogue',
        'form'              : forms.CatalogueForm(instance=Catalogue.objects.get(pk=id))
    });
    