from django.shortcuts import render
from consult_panel.models import *
from django.contrib.auth.decorators import user_passes_test
from admin_panel.forms import SessionForm
from admin_panel.user_tests import *


@user_passes_test(is_formateur)
def sessions_index(request):
    return render(request, 'admin_sessions_index.html', context={
        'page_title': 'Gestion des sessions',
        # .distinct('id') with MySQL (SQLite3 not supported)
        'sessions_list': Session.objects.filter(formation__catalogue__profile__user=request.user)
    })


@user_passes_test(is_formateur)
def sessions_detail(request, id):
    session = Session.objects.get(pk=id)
    return render(request, 'admin_sessions_detail.html', context={
        'page_title': session.formation.nom,
        # .distinct('id') with MySQL (SQLite3 not supported)
        'session': session
    })


@user_passes_test(is_formateur)
def sessions_add(request):
    return render(request, 'admin_sessions_add.html', {
        'page_title': 'Ajouter une session',
        'form': SessionForm()
    })


@user_passes_test(is_formateur)
def sessions_edit(request, id):
    return render(request, 'admin_sessions_edit.html', {
        'page_title': 'Editer une session',
        'form': SessionForm(instance=Session.objects.get(pk=id))
    })
