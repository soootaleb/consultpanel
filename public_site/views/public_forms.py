from django.contrib import messages
from django.contrib.auth import authenticate, login as lin
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from datetime import datetime
from mailer.mailer import EmailTemplate
from public_site import forms
from unique_linker.models import Unique
from django.views.decorators.csrf import csrf_exempt


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

@csrf_exempt
def password_forgot(request):
    if request.method == 'POST':
        form = forms.PasswordForgotForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=request.POST['username'])
            if user is not None:
                method = "public_site.views.public_pages/password_reset"
                params = { "user_id": user.id }
                unique = Unique(auteur=user, methode=method, params=params)
                unique.save()
                url = unique.get_url()
                msg = "Nous vous avons envoye un lien a l'adresse email suivante : " + str(user.email)
                messages.success(request, msg)
                email = EmailTemplate('password_reset', {'date', datetime.now().date})
                email.send([user.email], context={'first_name': user.first_name, 'unique_url': url})
            else:
                msg = "Nous n'avons pu trouve de compte assoscie a cet email."
                messages.error(request, msg)

            return redirect('public_login')

    context = {
        'page_title': 'Mot de passe oublie',
        'password_reset_form': forms.PasswordForgotForm(),
    }
    return render(request, 'public_pages_forgot_password.html', context=context)

@csrf_exempt
def password_reset(request):
    if request.method == 'POST':
        try:
            token = request.POST.get("token", None)
            user = User.objects.get(username=request.POST['username'])
            unique = Unique.objects.get(jeton=request.POST.get("token", None), perime=False, auteur=user)
            unique.perime = True
            unique.save()
            form = forms.PasswordResetForm(request.POST)
            if form.is_valid():
                if user is not None:
                    user.set_password(request.POST['password'])
                    user.save()
                    msg = "Votre mot de passe a bien ete modifie"
                    messages.success(request, msg)
                    return redirect('public_login')
        except:
            raise Http404

    raise Http404