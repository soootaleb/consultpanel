from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib import auth
from public_site import forms
from django.contrib import messages
from formtools.wizard.views import SessionWizardView
from consult_panel.models import Profile
from unique_linker.models import Unique
from mailer.mailer import EmailTemplate
from datetime import datetime

class RegistrationWizard(SessionWizardView):
    def get_template_names(self):
        if  self.request.user.is_authenticated():
            return redirect('admin_index')

        return ['public_pages_register.html']

    def done(self, form_list, **kwargs):
        if create_new_superformateur(self.request, form_list):
            messages.info(self.request, "Un email vous a été envoyé. Confirmez nous votre adresse email.")
            return redirect('admin_index')

        messages.warning(self.request, "Une erreur est survenue durant l'inscription. Réessayez plus tard.")
        return redirect('public_index')

def send_confirm_email_request(profile):
    if profile is not None:
        methode = 'consult_panel.models/Profile/validemail'
        #on check si il n'y a pas deja un lien actif:
        try:
            unique = Unique.objects.get(auteur=profile.user, methode=methode, params=profile.id)
            unique.delete()
        except:
            pass
        # creation du unique linker pour valider l'email:
        params = {"id": profile.id}
        unique = Unique(auteur=profile.user, methode=methode, params=params)
        unique.save()
        url = unique.get_url()
        email = EmailTemplate('confirm_email', {'date', datetime.now().date})
        email.send([profile.user.email], context={'first_name': profile.user.first_name, 'unique_url': url})


def create_new_superformateur(request, form_list):
    form_data = [form for form in form_list]
    user = form_data[0].save()
    superFormateurGroup, superFormateurGroupCreated = Group.objects.get_or_create(
        name='super_formateur')
    superFormateurGroup.user_set.add(user)
    centre_formation = form_data[1].save()
    profile = Profile.objects.create(
        user=user, centre_formation=centre_formation)
    profile.save()
    send_confirm_email_request(profile)
    return True


def public_index(request):
    return render(request, 'public_pages_landing.html')


def form(request, name):
    from . import public_forms
    if request.method == 'POST':
        response = getattr(public_forms, name)(request)
        return response if response is not None else redirect('public_index')
    else:
        messages.warning(request, 'Oops, vous vous êtes perdu...')
        return redirect('public_index')


def login(request):
    if request.user.is_authenticated():
        messages.info(request, "Vous êtes déjà connecté !")
        return redirect('public_index')
    context = {
        'page_title':   'Connexion',
        'login_form':   forms.LoginForm(auto_id=False),
    }
    return render(request, 'public_pages_login.html', context=context)


def logout(request):
    if not request.user.is_authenticated():
        messages.info(request, "Vous n'êtes pas connecté")
        return redirect('public_index')
    auth.logout(request)
    messages.success(request, "Vous êtes maintenant déconnecté")
    return redirect('public_index')


def forgot_password(request):
    return render(request, 'public_pages_forgot_password.html')
