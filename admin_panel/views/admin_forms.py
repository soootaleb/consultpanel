from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as lin # To avoid ambigous function name
from admin_panel import forms
from consult_panel.models import *
from django.contrib import messages

def formations_add(request):
    form = forms.FormationForm(request.POST);
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