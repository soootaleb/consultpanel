from django.shortcuts import render, redirect
from consult_panel.models import *
from django.contrib.auth.decorators import user_passes_test
from admin_panel.user_tests import *
from admin_panel.forms import *
import base64
from django.core.files.base import ContentFile
from django.contrib import messages


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
    profil = Profile.objects.get(user=request.user)
    if request.method == "POST":
        url = request.POST.get("url_base64", "")
        head, data = url.split(',',1)
        print("POST URL : "+data)
        if url != "":
            url_decoded = base64.b64decode(data)
            content = ContentFile(url_decoded)
            profil.signature.save(str(profil.user_id)+"_signature.png", content)
            profil.save()
            messages.success(request, 'Votre signature a bien été modifié.');
            return redirect('profil_index')
        else :
            messages.warning(request, 'Une erreur est survenu, merci de reessayer.')


    return render(request, 'admin_profil_signature_edit.html', {
        'profil' : profil,
        'page_title': 'Modifier votre signature',
    })

