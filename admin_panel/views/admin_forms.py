from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as lin # To avoid ambigous function name
from admin_panel import forms
from consult_panel.models import *
from django.contrib import messages

def formations_add(request):
    form = forms.FormationForm(request.POST);
    form.user = request.user
    if form.is_valid() :
        form.save();
        messages.success(request, 'La formation a bien été ajoutée');
        return redirect('/consult/formations')
    else :
        messages.warning(request, 'Merci de vérifier les informations');
        return render(request, 'admin_formations_add.html', context={'form' : form});
    
def formations_edit(request):
    form = forms.FormationForm(request.POST or None, instance=Formation.objects.get(pk=request.POST["formation_id"]));
    if form.is_valid() and form.instance is not None :
        form.save();
        messages.success(request, 'La formation a bien été modifiée');
        return redirect('/consult/formations/')
    else :
        messages.warning(request, 'Merci de vérifier les informations');
        return render(request, 'admin_formations_edit.html', context={'form' : form});
    
def catalogues_add(request):
    form = forms.CatalogueForm(request.POST);
    form.user = request.user
    if form.is_valid() :
        form.save();
        messages.success(request, 'Le catalogue a bien été ajoutée');
        return redirect('/consult/catalogues/')
    else :
        messages.warning(request, 'Merci de vérifier les informations');
        return render(request, 'admin_catalogues_add.html', context={'form' : form});
    
def catalogues_edit(request):
    form = forms.CatalogueForm(request.POST or None, instance=Catalogue.objects.get(pk=request.POST["catalogue_id"]));
    if form.is_valid() and form.instance is not None :
        form.save();
        messages.success(request, 'Le catalogue a bien été modifié');
        return redirect('/consult/catalogues/')
    else :
        messages.warning(request, 'Merci de vérifier les informations');
        return render(request, 'admin_catalogues_edit.html', context={'form' : form});
    
    
    
    
    
    
    
    
    
def sessions_add(request):
    form = forms.SessionForm(request.POST);
    if form.is_valid() :
        form.save();
        messages.success(request, 'La formation a bien été ajoutée');
        return redirect('sessions_index')
    else :
        messages.warning(request, 'Merci de vérifier les informations');
        return render(request, 'admin_formations_add.html', context={'form' : form});
    
def sessions_edit(request):
    form = forms.SessionForm(request.POST or None, instance=Session.objects.get(pk=request.POST["session_id"]));
    if form.is_valid() and form.instance is not None :
        form.save();
        messages.success(request, 'La formation a bien été modifiée');
        return redirect('sessions_index')
    else :
        messages.warning(request, 'Merci de vérifier les informations');
        return render(request, 'admin_sessions_edit.html', context={'form' : form});