from django.shortcuts import render, redirect
from consult_panel.models import *
from django.contrib import messages
from django.contrib.auth.decorators import permission_required

def index(request):
    return render(request, 'admin_pages_index.html', context={
        'page_title'        :   'Tableau de bord',
        'formation_list'    :   Formation.objects.all(),
    });

# Getting common forms routed here. Process is done in common_forms.py
def form(request, name):
    from . import admin_forms
    if request.method == 'POST' :
        response = getattr(admin_forms, name)(request)
        return response if response is not None else redirect('consult/')
    else :
        messages.warning(request, 'Oops, vous vous êtes perdu...')
        return redirect('consult/')   
    
def about(request):
    pass;

def contact(request):
    pass;