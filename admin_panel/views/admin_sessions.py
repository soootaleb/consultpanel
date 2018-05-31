from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from consult_panel.models import Session, Inscription, Formation
from consult_panel.models import Client, Cours
from documents.models import Convention
from admin_panel.forms import SessionForm, CoursForm, InscriptionForm
from admin_panel.user_tests import is_formateur


@user_passes_test(is_formateur)
def sessions_index(request):
    session_list = Session.objects.filter(
        formation__catalogue__profile__user=request.user).distinct()
    return render(request, 'admin_sessions_index.html', context={
        'page_title': 'Gestion des sessions',
        'sessions_list': session_list
    })


@user_passes_test(is_formateur)
def sessions_detail(request, session_id, tab):

    distincted_inscriptions = Inscription.objects \
        .filter(session__pk=session_id) \
        .distinct('client')

    cours = Cours.objects \
        .filter(session__pk=session_id) \
        .order_by('date_cours_debut')

    conventions_by_client = [
        {
            'client': inscription.client,
            'conventions': Convention.objects.filter(
                session__pk=session_id,
                client=inscription.client,
                cours__in=cours
            )
        }
        for inscription in distincted_inscriptions
    ]

    session = Session.objects.get(pk=session_id)
    session.inscriptions = Inscription.objects.filter(session=session)
    cours_form = CoursForm()
    inscription_form = InscriptionForm()
    inscription_form.fields['client'].queryset = Client.objects.filter(
        catalogue__profile__user=request.user)
    tabs = ['detail', 'inscriptions', 'docs']

    return render(request, 'admin_sessions_detail.html', context={
        'cours': cours,
        'page_title': session.formation.nom,
        'session': session,
        'form_add_cours': cours_form,
        'form_add_inscription': inscription_form,
        'active_tab': tab if tab in tabs else 'detail',
        'conventions_by_client': conventions_by_client
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

@user_passes_test(is_formateur)
def sessions_delete(request, id):
    session = get_object_or_404(Session, pk=id)
    session.delete()
    return redirect('sessions_index')

@user_passes_test(is_formateur)
def sessions_remove_course(request, session_id, tab, course_id):
    cours = get_object_or_404(Cours, pk=course_id)
    cours.delete()
    return redirect('sessions_detail', session_id, tab) if tab else redirect('sessions_detail', session_id)

@user_passes_test(is_formateur)
def sessions_remove_inscription(request, session_id, tab, inscription_id):
    inscription = get_object_or_404(Inscription, pk=inscription_id)
    inscription.delete()
    return redirect('sessions_detail', session_id, tab) if tab else redirect('sessions_detail', session_id)

