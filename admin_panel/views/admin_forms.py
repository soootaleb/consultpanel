from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as lin # To avoid ambigous function name
from admin_panel import forms
from django.contrib import messages

def formations_add(request):
    if request.method == 'POST' :
        form = forms.FormationForm(request.POST);
        if form.is_valid() :
            form.save();
            messages.success(request, 'La formation a bien été ajoutée');
            return redirect('/consult/formations')
        else :
            messages.warning(request, 'Merci de vérifier les informations');
            return render(request, 'admin_formations_add.html', context={'form' : form});
    else :
        return redirect('/consult');