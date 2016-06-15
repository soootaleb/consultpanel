from django.shortcuts import render
from consult_panel.models import *
from django.contrib.auth.decorators import user_passes_test
from admin_panel.forms import *
from admin_panel.user_tests import *


@user_passes_test(is_formateur)
def entreprises_index(request):
    return render(request, 'admin_entreprises_index.html', context={
                  'page_title':   'Gestion des entreprises',
                  'entreprises_list':   Entreprise.objects.all(),
                  })


@user_passes_test(is_formateur)
def entreprises_add(request):
    return render(request, 'admin_entreprises_add.html', {
                  'page_title': 'Ajouter une entreprise',
                  'form': EntrepriseForm()
                  })


@user_passes_test(is_formateur)
def entreprises_edit(request, id):
    return render(request, 'admin_entreprises_edit.html', {
                  'page_title': 'Editer une entreprise',
                  'form': EntrepriseForm(instance=Entreprise.objects.get(pk=id))
                  })
