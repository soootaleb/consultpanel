# coding: utf8

from django.contrib import messages
from django.shortcuts import render, redirect
from consult_panel.models import *
from admin_panel.user_tests import *
from django.contrib.auth.decorators import login_required, user_passes_test
import time, json

@user_passes_test(is_formateur)
def pages_index(request):
    cours_list = []
    cours = Cours.objects.filter(
        session__formation__catalogue__profile__user=request.user).select_related().distinct()
    for c in cours:
        cours_list.append({
            'title': c.session.formation.nom,
            'start': c.date_cours_debut.strftime('%Y-%m-%dT%H:%M%S'),
            'end': c.date_cours_fin.strftime('%Y-%m-%d'),
            'className': 'event-orange'
        })
    head = {
        'sessions': Session.objects.filter(formation__catalogue__profile__user=request.user).distinct().count(),
        'inscrits': Inscription.objects.filter(session__formation__catalogue__profile__user=request.user).distinct().count(),
        'formations': Formation.objects.filter(catalogue__profile__user=request.user).distinct().count(),
        'clients': Client.objects.filter(catalogue__profile__user=request.user).distinct().count(),
        'catalogues': Catalogue.objects.filter(profile__user=request.user).distinct().count(),
        'entreprises': Profile.objects.get(user=request.user).liste_entreprises.count(),
        'centres': Localisation.objects.filter(profile__user=request.user).distinct().count()
    }
    
    for key, value in head.items():
        if key != 'inscrits' and value == 0:
            messages.info(request, 'Pensez à rentrer toutes les données du menu sur la gauche afin de pouvoir générer vos convention')
            break

    return render(request, 'admin_pages_index.html', context={
        'page_title':   'Tableau de bord',
        'header':   False,
        'datas':   {
            'calendar_date': time.strftime('%Y-%m-%d'),
            'calendar_content': json.dumps(cours_list),
            'head': head
        },
    })


@user_passes_test(is_formateur)
def form(request, name):
    from . import admin_forms
    if request.method == 'POST':
        response = getattr(admin_forms, name)(request)
        return response if response is not None else redirect('consult/')
    else:
        messages.warning(request, 'Oops, vous vous êtes perdu...')
        return redirect('admin_index')
