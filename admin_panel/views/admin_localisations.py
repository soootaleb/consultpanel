from django.shortcuts import render, get_object_or_404, redirect
from consult_panel.models import *
from admin_panel.forms import *
from admin_panel.user_tests import *
from django.contrib.auth.decorators import user_passes_test


@user_passes_test(is_formateur)
def localisations_index(request):
    return render(request, 'admin_localisations_index.html', context={
                  'page_title':   'Gestion des centres',
                  'centres_list':   Localisation.objects.filter(profile__user=request.user).distinct(),
                  })


@user_passes_test(is_formateur)
def localisations_add(request):
    return render(request, 'admin_localisations_add.html', {
                  'page_title': 'Ajouter un centre',
                  'form': LocalisationForm()
                  })


def localisations_edit(request, id):
    return render(request, 'admin_localisations_edit.html', {
                  'page_title': 'Editer un centre',
                  'form': LocalisationForm(instance=Localisation.objects.get(pk=id))
                  })

@user_passes_test(is_formateur)
def localisations_delete(request, id):
    localisation = get_object_or_404(Localisation, id)
    localisation.delete()
    return redirect('localisations_index')
