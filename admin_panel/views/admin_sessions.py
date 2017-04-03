from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from consult_panel.models import *
from documents.models import Convention
from admin_panel.forms import SessionForm, CoursForm, InscriptionForm
from admin_panel.user_tests import *


@user_passes_test(is_formateur)
def sessions_index(request):
    session_list = Session.objects.filter(
        formation__catalogue__profile__user=request.user).distinct()
    return render(request, 'admin_sessions_index.html', context={
        'page_title': 'Gestion des sessions',
        'sessions_list': session_list
    })


@user_passes_test(is_formateur)
def sessions_detail(request, id, tab):
    session = Session.objects.get(pk=id)
    session.cours = Cours.objects.filter(session=session)
    session.inscriptions = Inscription.objects.filter(session=session)
    cours_form = CoursForm()
    cours_form.fields['localisation'].queryset = Localisation.objects.filter(
        profile__user=request.user).distinct()
    inscription_form = InscriptionForm()
    inscription_form.fields['client'].queryset = Client.objects.filter(
        catalogue__profile__user=request.user)
    return render(request, 'admin_sessions_detail.html', context={
        'page_title': session.formation.nom,
        'session': session,
        'form_add_cours': cours_form,
        'form_add_inscription': inscription_form,
        'active_tab': tab if tab in ['detail', 'inscriptions', 'docs'] else 'detail',
        'conventions_list': Convention.objects.filter(client__inscription__session__id=id).distinct()
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
    session_form = SessionForm(instance=Session.objects.get(pk=id))
    session_form.fields['formation'].queryset = Formation.objects.filter(
        catalogue__profile__user=request.user).distinct()
    return render(request, 'admin_sessions_edit.html', {
        'page_title': 'Editer une session',
        'form': session_form
    })
