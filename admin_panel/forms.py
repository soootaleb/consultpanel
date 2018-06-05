# coding: utf-8

from datetime import timedelta
from datetime import datetime as dt
from consult_panel.models import *
from documents.models import *
from django.forms import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

import pytz

class InscriptionForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-10'
        self.helper.add_input(Submit('submit', 'Ajouter'))
        super(InscriptionForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Inscription
        fields = ['nom', 'prenom', 'client']
        labels = {'nom': 'Nom : ', 'prenom': 'Prénom : ',
                  'client': 'Client associé : '}


class ClientForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-10'
        self.helper.add_input(Submit('submit', 'Envoyer'))
        super(ClientForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Client
        fields = [
            'nom',
            'catalogue',
            'entreprise',
            'representant_prenom',
            'representant_nom'
        ]
        labels = {
            'label': 'Nom : ',
            'catalogue': 'Catalogue Associé : ',
            'entreprise': 'Entreprise Associée : '
        }


class FileForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-10'
        self.helper.add_input(Submit('submit', 'Envoyer'))
        super(FileForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Template
        fields = ['label', 'document', 'type']
        labels = {'label': 'Titre : ', 'document': 'Fichier : '}


class CoursForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-10'
        self.helper.add_input(Submit('submit', 'Ajouter'))
        super(CoursForm, self).__init__(*args, **kwargs)
        self.fields['date_cours_debut'].initial = (dt.now() + timedelta(days=1)).replace(hour=9, minute=0, second=0)
        self.fields['date_cours_fin'].initial = (dt.now() + timedelta(days=1)).replace(hour=17, minute=0, second=0)

    class Meta:
        model = Cours
        fields = ['date_cours_debut', 'date_cours_fin']
        labels = {
            'date_cours_debut': 'Début : ',
            'date_cours_fin': 'Fin : ',
            'session': 'Session de formation'
        }


class FormationForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-10'
        self.helper.add_input(Submit('submit', 'Sauvegarder'))
        super(FormationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Formation
        fields = ['nom', 'description', 'prix_ht', 'action_formation']
        labels = {
            'nom': 'Nom : ',
            'description': 'Description : ',
            'prix_ht': 'Prix H.T (€) : ',
        }


class CatalogueForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-10'
        self.helper.add_input(Submit('submit', 'Sauvegarder'))
        super(CatalogueForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Catalogue
        fields = ['nom', 'liste_formations']
        widgets = {
            'liste_formations': CheckboxSelectMultiple
        }
        labels = {
            'nom': 'Nom : ',
            'liste_formations': 'Liste des formations : ',
        }


class SessionForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-10'
        self.helper.add_input(Submit('submit', 'Ajouter'))
        super(SessionForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Session
        fields = ['formation']


class EntrepriseForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-10'
        self.helper.add_input(Submit('submit', 'Sauvegarder'))
        super(EntrepriseForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Entreprise
        fields = ['nom', 'adresse', 'ville', 'code_postal', 'telephone', 'siret']


class CentreFormationForm(ModelForm):

    nom = CharField(required=True, label="Nom de l'entreprise :")
    siret = CharField(required=True, label="Numéro de siret :")
    adresse = CharField(required=True, label="Adresse :")
    ville = CharField(required=True, label="Ville :")
    code_postal = CharField(required=True, label="Code Postal :")
    telephone = CharField(required=True, label="Téléphone :")

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-10'
        self.helper.add_input(Submit('submit', 'Sauvegarder'))
        super(CentreFormationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = CentreFormation
        fields = ['nom', 'siret', 'adresse', 'ville',
                  'code_postal', 'telephone']


class ChangeUserPasswordForm(Form):

    old_password = CharField(
        required=True,
        widget=PasswordInput,
        label="Ancien mot de passe :"
    )
    new_password = CharField(
        required=True,
        widget=PasswordInput,
        label="Nouveau mot de passe :"
    )
    confirm_new_password = CharField(
        required=True,
        widget=PasswordInput,
        label="Confirmation du mot de passe :"
    )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-10'
        self.helper.add_input(Submit('submit', 'Sauvegarder'))
        self.user = kwargs.pop('user')
        super(ChangeUserPasswordForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(ChangeUserPasswordForm, self).clean()
        old_password = cleaned_data.get('old_password')
        new_password = cleaned_data.get('new_password', '')
        confirm_new_password = cleaned_data.get('confirm_new_password', '')

        if self.user is None:
            self.add_error("old_password", "Impossible de verifier le mot de passe. Reesayer plus tard.")

        if new_password != confirm_new_password:
            msg = "Les deux emails ne correspondent pas."
            self.add_error("new_password", msg)
            self.add_error("confirm_new_password", msg)

        if len(new_password) < 6:
            self.add_error("new_password", "Le mot de passe doit contenir au moins 6 caractères.")

        if not self.user.check_password(old_password):
            self.add_error("old_password", "Le mot de passe ne correspond pas.")

        return cleaned_data

    def save(self, commit=True):
        if self.user is not None:
            self.user.set_password(self.cleaned_data.get('new_password'))
        if commit:
            self.user.save()
        return self.user
