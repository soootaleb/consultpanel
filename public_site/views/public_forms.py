from django.shortcuts import render
from django.contrib.auth import authenticate, login as lin # To avoid ambigous function name
from public_site import forms
from django.contrib import messages

def login(request):
    if request.method == 'POST' :
        form = forms.LoginForm(request.POST);
        if form.is_valid() :
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                # the password verified for the user
                if user.is_active:
                    lin(request, user);
                    message = "Bienvenue, " + user.first_name if user.first_name != '' else "Bienvenue, " + user.username;
                    messages.success(request, message);
                    context = {
                        'page_title'        :   'Connexion',
                    }
                    if user.groups.filter(name='consultants').exists() :
                        return render(request, 'admin_pages_index.html', context=context);
                    else :
                        return render(request, 'public_pages_index.html', context=context);
                else:
                    return HttpResponseForbidden("Désolé, mais votre compte n'est plus actif")
            else:
                context = {
                    'page_title'        :   'Connexion',
                    'login_form'        :   form,
                }
                messages.warning(request, "Merci de vérifier les informations");
                return render(request, 'public_pages_login.html', context=context);
        else :
            context = {
                'page_title'        :   'Connexion',
            }
            messages.warning(request, "Merci de vérifier les informations");
            return render(request, 'public_pages_login.html', context=context);