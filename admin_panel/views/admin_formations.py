from django.shortcuts import render
from consult_panel.models import *
from admin_panel.forms import forms
from admin_panel.user_tests import *
from django.contrib.auth.decorators import user_passes_test


@user_passes_test(is_formateur)
def formations_index(request):
    return render(request, 'admin_formations_index.html', context={
                  'page_title':   'Gestion des formations',
                  'formations_list':   Formation.objects.all(),
                  })


@user_passes_test(is_formateur)
def formations_add(request):
    return render(request, 'admin_formations_add.html', {
                  'page_title': 'Ajouter une formation',
                  'form': forms.FormationForm()
                  })


@user_passes_test(is_formateur)
def formations_edit(request, id):
    return render(request, 'admin_formations_edit.html', {
                  'page_title': 'Editer une formation',
                  'form': forms.FormationForm(instance=Formation.objects.get(pk=id))
                  })
