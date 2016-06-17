from django.shortcuts import render
from consult_panel.models import *
from django.contrib.auth.decorators import user_passes_test
from admin_panel.forms import SessionForm, CoursForm
from admin_panel.user_tests import *


@user_passes_test(is_formateur)
def sessions_index(request):
    return render(request, 'admin_sessions_index.html', context={
        'page_title': 'Gestion des sessions',
        'sessions_list': Session.objects.filter(formation__catalogue__profile__user=request.user).distinct()
    })


@user_passes_test(is_formateur)
def sessions_detail(request, id):
    session = Session.objects.get(pk=id)
    session.cours = Cours.objects.filter(session=session)
    return render(request, 'admin_sessions_detail.html', context={
        'page_title': session.formation.nom,
        'session': session,
        'form_add_cours': CoursForm()
    })


@user_passes_test(is_formateur)
def sessions_add(request):
    session_form = SessionForm()
    session_form.fields['formation'].queryset = Formation.objects.filter(
        catalogue__profile__user=request.user).distinct()
    return render(request, 'admin_sessions_add.html', {
        'page_title': 'Ajouter une session',
        'form': session_form
    })


@user_passes_test(is_formateur)
def sessions_edit(request, id):
    return render(request, 'admin_sessions_edit.html', {
        'page_title': 'Editer une session',
        'form': SessionForm(instance=Session.objects.get(pk=id))
    })
