from django.shortcuts import render
from consult_panel.models import *
from django.contrib.auth.decorators import user_passes_test
from admin_panel.user_tests import *
from admin_panel.forms import *

@user_passes_test(is_formateur)
def profil_index(request):
    profil = Profile.objects.get(user=request.user)
    return render(request, 'admin_profil_index.html', context={
        'user':   request.user,
        'profil': profil,
        'page_title':   'Mon profil'
    })

@user_passes_test(is_formateur)
def profil_edit(request, id):
    centre_form = CentreFormationForm(instance=CentreFormation.objects.get(pk=id))
    return render(request, 'admin_profil_edit.html', {
        'page_title': 'Modifier le profil',
        'form': centre_form
    })

@user_passes_test(is_formateur)
def profil_signature_edit(request, id):
    return render(request, 'admin_profil_signature_edit.html', {
        'page_title': 'Modifier votre signature',
    })

