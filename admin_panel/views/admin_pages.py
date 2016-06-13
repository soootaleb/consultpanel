# coding: utf8

from django.shortcuts import render, redirect
from consult_panel.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from admin_panel.user_tests import *


@user_passes_test(is_formateur)
def pages_index(request):
    return render(request, 'admin_pages_index.html', context={
        'page_title':   'Tableau de bord',
        'header':   False,
        'formation_list':   Formation.objects.all(),
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
