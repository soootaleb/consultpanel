from django.contrib import messages
from django.contrib.auth import authenticate, login as lin
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect

from public_site import forms


def register(request):
    pass


def login(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST[
                                'username'], password=request.POST['password'])
            if user is not None:
                # the password verified for the user
                if user.is_active:
                    lin(request, user)
                    message = "Bienvenue, " + \
                        user.first_name if user.first_name != '' else "Bienvenue, " + user.username
                    messages.success(request, message)
                    context = {
                        'page_title':   'Connexion',
                    }
                    if user.groups.filter(name='consultants').exists():
                        return render(request, 'admin_pages_index.html', context=context)
                    else:
                        return render(request, 'admin_pages_index.html', context=context)
                else:
                    messages.warning(request, "Votre compte n'est pas activé.")
                    return redirect('public_login')
            else:
                context = {
                    'page_title':   'Connexion',
                    'login_form':   form,
                }
                messages.warning(request, "Merci de vérifier les informations")
                return render(request, 'public_pages_login.html', context=context)
        else:
            context = {
                'page_title':   'Connexion',
            }
            messages.warning(request, "Merci de vérifier les informations")
            return render(request, 'public_pages_login.html', context=context)