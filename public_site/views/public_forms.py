from django.contrib import messages
from django.contrib.auth import authenticate, login as lin
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from public_site import forms


def register(request):
    pass


def login(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['username'], password=request.POST['password'])

            if user is not None:
                # the password verified for the user
                if user.is_active:
                    lin(request, user)
                    message = "Bienvenue, " + \
                        user.first_name if user.first_name != '' else "Bienvenue, " + user.username
                    messages.success(request, message)
                    return redirect('admin_index')
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


def password_forgot(request):
    if request.method == 'POST':
        form = forms.PasswordResetForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=request.POST['username'])
            if user is not None:
                generator = PasswordResetTokenGenerator()
                token = generator.make_token(user)
                msg = "Nous vous avons envoye un lien a l'adresse email suivante : " + str(user.username)
                messages.success(request, msg)
                print(token)
                return redirect('public_login')

    msg = "Nous n'avons pu trouve de compte assoscie a cet email."
    messages.error(request, msg)
    context = {
        'page_title': 'Mot de passe oublie',
        'password_reset_form': form,
    }
    return render(request, 'public_pages_forgot_password.html', context=context)

def password_reset(request):
    if request.method == 'POST':
        form = forms.PasswordResetForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=request.POST['username'])
            if user is not None:
                user.set_password(request.POST['password'])
                user.save()
                msg = "Votre mot de passe a bien ete mnodifie"
                messages.success(request, msg)
                return redirect('public_login')
    raise Http404