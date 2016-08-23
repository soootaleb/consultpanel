from django.shortcuts import render, redirect
# To avoid ambigous function name
from django.contrib.auth import authenticate, login as lin
from admin_panel import forms
from consult_panel.models import *
from documents.models import Convention
from documents.models import *
from django.contrib import messages


def localisations_add(request):
    form = forms.LocalisationForm(request.POST)
    form.instance.profile = Profile.objects.get(user=request.user)
    if form.is_valid():
        form.save()
        messages.success(request, 'Le centre a bien été ajoutée')
        return redirect('/consult/localisations/')
    else:
        messages.warning(request, 'Merci de vérifier les informations')
        return render(request, 'admin_localisations_add.html', context={'form': form})


def localisations_edit(request):
    form = forms.LocalisationForm(request.POST or None, instance=Localisation.objects.get(
        pk=request.POST["localisation_id"]))
    if form.is_valid() and form.instance is not None:
        form.save()
        messages.success(request, 'Le centre a bien été modifié')
        return redirect('/consult/localisations/')
    else:
        messages.warning(request, 'Merci de vérifier les informations')
        return render(request, 'admin_localisations_edit.html', context={'form': form})


def file_upload(request):
    form = forms.FileForm(request.POST, request.FILES)
    form.instance.profile = Profile.objects.get(user=request.user)
    form.slug = 'this-is-my-test-slug'
    if form.is_valid():
        form.save()
        messages.success(request, 'Le document a bien été ajouté')
        return redirect('/consult/preferences')
    else:
        messages.warning(request, 'Une erreur a été rencontrée')
        return render(request, 'admin_preferences_index.html', context={
            'user':   request.user,
            'page_title':   'Préférences',
            'form': form,
            'active_tab': 'add',
            'dg_types':   DocumentType.objects.all(),
            'dg_templates':   Template.objects.all()
        })


def formations_add(request):
    form = forms.FormationForm(request.POST)
    form.user = request.user
    if form.is_valid():
        form.save()
        goc = Catalogue.objects.get_or_create(
            profile__user=request.user, nom='main')
        goc[0].liste_formations.add(
            Formation.objects.get(pk=form.instance.id))
        if goc[1]:
            Profile.objects.get(user=request.user).liste_catalogues.add(goc[0])
        messages.success(request, 'La formation a bien été ajoutée')
        return redirect('/consult/formations')
    else:
        messages.warning(request, 'Merci de vérifier les informations')
        return render(request, 'admin_formations_add.html', context={'form': form})


def formations_edit(request):
    form = forms.FormationForm(request.POST or None, instance=Formation.objects.get(
        pk=request.POST["formation_id"]))
    if form.is_valid() and form.instance is not None:
        form.save()
        messages.success(request, 'La formation a bien été modifiée')
        return redirect('/consult/formations/')
    else:
        messages.warning(request, 'Merci de vérifier les informations')
        return render(request, 'admin_formations_edit.html', context={'form': form})


def catalogues_add(request):
    form = forms.CatalogueForm(request.POST)
    if form.is_valid():
        form.save()
        Profile.objects.get(user=request.user).liste_catalogues.add(
            Catalogue.objects.get(pk=form.instance.id))
        messages.success(request, 'Le catalogue a bien été ajoutée')
        return redirect('/consult/catalogues/')
    else:
        messages.warning(request, 'Merci de vérifier les informations')
        form.fields['liste_formations'].queryset = Formation.objects.filter(
            catalogue__profile__user=request.user).distinct()
        return render(request, 'admin_catalogues_add.html', context={'form': form})


def catalogues_edit(request):
    form = forms.CatalogueForm(request.POST or None, instance=Catalogue.objects.get(
        pk=request.POST["catalogue_id"]))
    if form.is_valid() and form.instance is not None:
        form.save()
        messages.success(request, 'Le catalogue a bien été modifié')
        return redirect('/consult/catalogues/')
    else:
        messages.warning(request, 'Merci de vérifier les informations')
        form.fields['liste_formations'].queryset = Formation.objects.filter(
            catalogue__profile__user=request.user).distinct()
        return render(request, 'admin_catalogues_edit.html', context={'form': form})


def sessions_add(request):
    form = forms.SessionForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'La session a bien été ajoutée')
        return redirect('sessions_index')
    else:
        messages.warning(request, 'Merci de vérifier les informations')
        form.fields['formation'].queryset = Formation.objects.filter(
            catalogue__profile__user=request.user).distinct()
        return render(request, 'admin_formations_add.html', context={'form': form})


def sessions_edit(request):
    form = forms.SessionForm(request.POST or None, instance=Session.objects.get(
        pk=request.POST["session_id"]))
    if form.is_valid() and form.instance is not None:
        form.save()
        messages.success(request, 'La formation a bien été modifiée')
        return redirect('sessions_index')
    else:
        messages.warning(request, 'Merci de vérifier les informations')
        form.fields['formation'].queryset = Formation.objects.filter(
            catalogue__profile__user=request.user).distinct()
        return render(request, 'admin_sessions_edit.html', context={'form': form})


def formateurs_add(request):
    form = forms.ProfileForm(request.POST)
    if form.is_valid() and form.instance is not None:
        form.save()
        messages.success(request, 'Le formateur a bien été ajouté')
        return redirect('formateurs_index')
    else:
        messages.warning(request, 'Merci de vérifier les informations')
        return render(request, 'admin_formateurs_edit.html', context={'form': form})


def formateurs_edit(request):
    form = forms.ProfileForm(request.POST or None, instance=Profile.objects.get(
        pk=request.POST["profile_id"]))
    if form.is_valid() and form.instance is not None:
        form.save()
        messages.success(request, 'Le formateur a bien été modifié')
        return redirect('formateurs_index')
    else:
        messages.warning(request, 'Merci de vérifier les informations')
        return render(request, 'admin_formateurs_edit.html', context={'form': form})


def clients_add(request):
    form = forms.ClientForm(request.POST)
    if form.is_valid() and form.instance is not None:
        form.save()
        messages.success(request, 'Le client a bien été ajouté')
        return redirect('clients_index')
    else:
        messages.warning(request, 'Merci de vérifier les informations')
        form.fields['catalogue'].queryset = Catalogue.objects.filter(
            profile__user=request.user).exclude(nom='main')
        form.fields['entreprise'].queryset = Entreprise.objects.filter(
            profile__user=request.user)
        return render(request, 'admin_clients_add.html', context={'form': form})


def clients_edit(request):
    form = forms.ClientForm(request.POST or None, instance=Client.objects.get(
        pk=request.POST["client_id"]))
    if form.is_valid() and form.instance is not None:
        form.save()
        messages.success(request, 'Le client a bien été modifié')
        return redirect('clients_index')
    else:
        messages.warning(request, 'Merci de vérifier les informations')
        form.fields['catalogue'].queryset = Catalogue.objects.filter(
            profile__user=request.user).exclude(nom='main')
        form.fields['entreprise'].queryset = Entreprise.objects.filter(
            profile__user=request.user)
        return render(request, 'admin_clients_edit.html', context={'form': form})


def cours_add(request):
    form = forms.CoursForm(request.POST)
    form.instance.session = Session.objects.get(pk=request.POST["session_id"])
    if form.is_valid():
        form.save()
        messages.success(request, 'Le cours a bien été ajouté')
        return redirect('sessions_detail', id=request.POST["session_id"])
    else:
        messages.warning(request, 'Merci de vérifier les informations')
        form.fields['localisation'].queryset = Localisation.objects.filter(
            profile__user=request.user).distinct()
        return render(request, 'admin_session_detail.html', context={'form_add_cours': form, 'form_add_inscription': forms.InscriptionForm()})


def inscriptions_add(request):
    form = forms.InscriptionForm(request.POST)
    form.instance.session = Session.objects.get(pk=request.POST["session_id"])
    if form.is_valid():
        form.save()
        Convention.objects.get_or_create(
            session=form.instance.session,
            client=form.instance.client
        )
        messages.success(request, 'L\'inscription a bien été ajoutée')
        return redirect('sessions_detail', id=request.POST["session_id"], tab='inscriptions')
    else:
        messages.warning(request, 'Merci de vérifier les informations')
        form.fields['client'].queryset = Client.objects.filter(
            catalogue__profile__user=request.user)
        return render(request, 'admin_sessions_detail.html', context={'form_add_inscription': form,
                                                                      'form_add_cours': forms.CoursForm(),
                                                                      'active_tab': 'inscriptions'
                                                                      })


def entreprises_add(request):
    form = forms.EntrepriseForm(request.POST)
    if form.is_valid() and form.instance is not None:
        form.save()
        Profile.objects.get(
            user=request.user).liste_entreprises.add(form.instance)
        messages.success(request, 'L\'entreprise a bien été ajoutée')
        return redirect('entreprises_index')
    else:
        messages.warning(request, 'Merci de vérifier les informations')
        return render(request, 'admin_entreprises_edit.html', context={'form':
                                                                       form})


def entreprises_edit(request):
    form = forms.EntrepriseForm(request.POST or None, instance=Entreprise.objects.get(
        pk=request.POST["entreprise_id"]))
    if form.is_valid() and form.instance is not None:
        form.save()
        messages.success(request, 'L\'entreprise a bien été modifiée')
        return redirect('entreprises_index')
    else:
        messages.warning(request, 'Merci de vérifier les informations')
        return render(request, 'admin_entreprises_edit.html', context={'form':
                                                                       form})

