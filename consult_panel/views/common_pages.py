from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as lin, logout as lout # To avoid ambigous function name
from consult_panel import forms
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'common_pages_index.html')

# Getting common forms routed here. Process is done in common_forms.py
def form(request, name):
    from . import common_forms
    if request.method == 'POST' :
        response = getattr(common_forms, name)(request)
        return response if response is not None else redirect('/')
    else :
        messages.warning(request, 'Oops, vous vous êtes perdu...')
        return redirect('/')

def login(request):
    if request.user.is_authenticated():
        messages.info(request, "Vous êtes déjà connecté !")
        return redirect('/')
    context = {
        'page_title'        :   'Connexion',
        'login_form'        :   forms.LoginForm(auto_id=False),
    }
    return render(request, 'common_pages_login.html', context=context);
    
def logout(request):
    if not request.user.is_authenticated():
        messages.info(request, "Vous n'êtes pas connecté")
        return redirect('/')
    lout(request)
    messages.success(request, "Vous êtes maintenant déconnecté");
    return redirect('/')

def action(request):
    return render(request, 'common_pages_login.html')

def todo(request):
    return render(request, 'common_pages_todo.html')