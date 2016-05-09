from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as lin, logout as lout # To avoid ambigous function name
from public_site import forms
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'public_pages_index.html')

# Getting common forms routed here. Process is done in public_forms.py
def form(request, name):
    from . import public_forms
    if request.method == 'POST' :
        response = getattr(public_forms, name)(request)
        return response if response is not None else redirect('public_index')
    else :
        messages.warning(request, 'Oops, vous vous êtes perdu...')
        return redirect('public_index')

def login(request):
    if request.user.is_authenticated():
        messages.info(request, "Vous êtes déjà connecté !")
        return redirect('public_index')
    context = {
        'page_title'        :   'Connexion',
        'login_form'        :   forms.LoginForm(auto_id=False),
    }
    return render(request, 'public_pages_login.html', context=context);
    
def logout(request):
    if not request.user.is_authenticated():
        messages.info(request, "Vous n'êtes pas connecté")
        return redirect('public_index')
    lout(request)
    messages.success(request, "Vous êtes maintenant déconnecté");
    return redirect('public_index')

