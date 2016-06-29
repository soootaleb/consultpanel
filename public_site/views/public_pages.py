from django.shortcuts import render, redirect
# To avoid ambigous function name
from django.contrib.auth.models import Group
from django.contrib import auth
from public_site import forms
from django.contrib import messages
from formtools.wizard.views import SessionWizardView
from consult_panel.models import Profile, Catalogue, CentreFormation


class RegistrationWizard(SessionWizardView):
    def get_template_names(self):
        return ['public_pages_register.html']

    def done(self, form_list, **kwargs):
        if create_new_superformateur(self.request, form_list):
            return redirect('admin_index')
        return redirect('public_index')


def create_new_superformateur(request, form_list):
    form_data = [form for form in form_list]
    user = form_data[0].save()
    superFormateurGroup, superFormateurGroupCreated = Group.objects.get_or_create(name='super_formateur')
    superFormateurGroup.user_set.add(user)
    centre_formation = form_data[1].save()
    profile = Profile.objects.create(user=user, centre_formation=centre_formation)
    profile.liste_catalogues.add(Catalogue.objects.create(nom="default"))
    profile.save()
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    auth.login(request, user)
    return True

def public_index(request):
    return render(request, 'public_pages_index.html')

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
    logout(request)
    messages.success(request, "Vous êtes maintenant déconnecté")
    return redirect('public_index')
