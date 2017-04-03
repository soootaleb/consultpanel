from django.shortcuts import render, get_object_or_404, redirect
from consult_panel.models import *
from django.contrib.auth.decorators import user_passes_test
from admin_panel.forms import ClientForm
from admin_panel.user_tests import *


@user_passes_test(is_formateur)
def clients_index(request):
    return render(request, 'admin_clients_index.html', context={
        'page_title': 'Gestion des clients',
        'clients_list': Client.objects.filter(catalogue__profile__user=request.user)
    })


@user_passes_test(is_formateur)
def clients_add(request):
    client_form = ClientForm()
    client_form.fields['catalogue'].queryset = Catalogue.objects.filter(
        profile__user=request.user).exclude(nom='main')
    client_form.fields['entreprise'].queryset = Entreprise.objects.filter(
        profile__user=request.user)
    return render(request, 'admin_clients_add.html', {
        'page_title': 'Ajouter un client',
        'form': client_form
    })


@user_passes_test(is_formateur)
def clients_edit(request, id):
    client_form = ClientForm(instance=Client.objects.get(pk=id))
    client_form.fields['catalogue'].queryset = Catalogue.objects.filter(
        profile__user=request.user).exclude(nom='main')
    client_form.fields['entreprise'].queryset = Entreprise.objects.filter(
        profile__user=request.user)
    return render(request, 'admin_clients_edit.html', {
        'page_title': 'Modifier un client',
        'form': client_form
    })

@user_passes_test(is_formateur)
def clients_delete(request, id):
    client = get_object_or_404(Client, id)
    client.delete()
    return redirect('clients_index')