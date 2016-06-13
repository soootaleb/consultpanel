from django.shortcuts import render
from consult_panel.models import *
from django.contrib.auth.decorators import user_passes_test
from consult_panel.forms import ProfileForm
from admin_panel.user_tests import *


@user_passes_test(is_formateur)
def clients_index(request):
    return render(request, 'admin_clients_index.html', context={
        'page_title': 'Gestion des clients',
        'clients_list': Profile.objects.all()
    })


@user_passes_test(is_formateur)
def clients_add(request):
    return render(request, 'admin_clients_add.html', {
        'page_title': 'Ajouter un client',
        'form': ProfileForm()
    })


@user_passes_test(is_formateur)
def clients_edit(request, id):
    return render(request, 'admin_clients_edit.html', {
        'page_title': 'Editer un client',
        'form': ProfileForm(instance=Profile.objects.get(pk=id))
    })
