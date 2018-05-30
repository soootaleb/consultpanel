from django.shortcuts import render, get_object_or_404, redirect
from consult_panel.models import *
from django.contrib.auth.decorators import user_passes_test
from admin_panel.forms import *
from admin_panel.user_tests import *


@user_passes_test(is_formateur)
def catalogues_index(request):
    return render(request, 'admin_catalogues_index.html', context={
        'page_title':   'Gestion des catalogues',
        'catalogues_list':   Catalogue.objects.filter(profile__user=request.user).exclude(nom='main').distinct(),
    })


@user_passes_test(is_formateur)
def catalogues_detail(request, id):
    catalogue = Catalogue.objects.get(pk=id)
    return render(request, 'admin_catalogues_detail.html', context={
        'page_title':   catalogue.nom,
        'catalogue': catalogue
    })


@user_passes_test(is_formateur)
def catalogues_add(request):
    catalogue_form = CatalogueForm()
    catalogue_form.fields['liste_formations'].queryset = Formation.objects.filter(
        catalogue__profile__user=request.user).distinct()
    return render(request, 'admin_catalogues_add.html', {
        'page_title': 'Ajouter un catalogue',
        'form': catalogue_form
    })


@user_passes_test(is_formateur)
def catalogues_edit(request, id):
    catalogue_form = CatalogueForm(instance=Catalogue.objects.get(pk=id))
    catalogue_form.fields['liste_formations'].queryset = Formation.objects.filter(
        catalogue__profile__user=request.user).distinct()
    return render(request, 'admin_catalogues_edit.html', {
        'page_title': 'Editer un catalogue',
        'form': catalogue_form
    })

@user_passes_test(is_formateur)
def catalogues_delete(request, id):
    catalogue = get_object_or_404(Catalogue, pk=id)
    catalogue.delete()
    return redirect('catalogues_index')

@user_passes_test(is_formateur)
def catalogues_remove_formation(request, id_catalogue, id_formation):
    catalogue = get_object_or_404(Catalogue, pk=id_catalogue)
    formation = get_object_or_404(Formation, pk=id_formation)
    catalogue.liste_formations.remove(formation)
    return redirect('catalogues_detail', id_catalogue)
