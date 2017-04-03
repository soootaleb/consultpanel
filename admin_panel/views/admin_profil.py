from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from admin_panel.user_tests import *
from admin_panel.forms import *
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
    form = CentreFormationForm(request.POST or None, instance=CentreFormation.objects.get(pk=id))
    if request.method == "POST":
        if form.is_valid() and form.instance is not None:
            form.save()
            messages.success(request, 'Les informations ont bien été modifiées')
            return redirect('profil_index')
        else:
            messages.warning(request, 'Merci de vérifier les informations')
    return render(request, 'admin_profil_edit.html', context={'form': form, 'page_title': 'Modifier le profil'})

@user_passes_test(is_formateur)
def profil_password_edit(request):
    form = ChangeUserPasswordForm(request.POST or None, user=request.user)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre mot de passe a bien été modifiées')
            return redirect('profil_index')
        else:
            messages.warning(request, 'Merci de vérifier les informations')
    return render(request, 'admin_profil_edit.html', context={'form': form,
                                                              'page_title': 'Modifier votre mot de passe'})


@user_passes_test(is_formateur)
def profil_signature_edit(request):
    profil = Profile.objects.get(user=request.user)
    if request.method == "POST":
        image_base64 = request.POST.get("url_base64", "")
        if image_base64 != "":
            profil.signature_base64 = image_base64
            profil.save()
            messages.success(request, 'Votre signature a bien été modifié.')
            return redirect('profil_index')
        else :
            messages.warning(request, 'Une erreur est survenu, merci de reessayer.')


    return render(request, 'admin_profil_signature_edit.html', {
        'profil' : profil,
        'page_title': 'Modifier votre signature',
    })

