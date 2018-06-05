# coding: utf-8

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from django import forms
from django.contrib.auth import authenticate
from consult_panel.models import *


class RegistrationForm(forms.ModelForm):
    first_name = forms.CharField(required=True, label='Prénom')
    last_name = forms.CharField(required=True, label='Nom')
    username = forms.EmailField(required=True, label='E-mail')
    password = forms.CharField(widget=forms.PasswordInput, label='Mot de passe')

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_show_labels = False
        self.helper.field_class = 'col-xs-12'

        layout = self.helper.layout = Layout()
        for field_name, field in self.fields.items():
            layout.append(Field(field_name, placeholder=field.label))
        self.helper.form_show_labels = False

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.email = user.username
        # user.is_active = False
        user.is_active = True  # Disable email activation
        if commit:
            user.save()
            user = authenticate(username=user.username, password=self.cleaned_data['password'])
        return user


class CentreFormationForm(forms.ModelForm):
    nom = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': "Nom de l'entreprise"}))
    adresse = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'id': 'centre-formation-address',
            'placeholder': "Adresse"
        }))
    ville = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'id': 'centre-formation-city',
            'placeholder': "Ville"
        }))
    code_postal = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'id': 'centre-formation-zip',
            'placeholder': "Code Postal"
        }))
    telephone = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': "Téléphone (Facultatif)"
        }))
    siret = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': "Numéro de siret (Facultatif)"
        }))
    rgpd_generate_conventions = forms.BooleanField(
        required=True,
        label='Vous acceptez que vos données soient utilisées pour générer vos conventions.')

    def __init__(self, *args, **kwargs):
        super(CentreFormationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.field_class = 'col-xs-12'
        self.fields['nom'].label = False
        self.fields['adresse'].label = False
        self.fields['ville'].label = False
        self.fields['code_postal'].label = False
        self.fields['telephone'].label = False
        self.fields['siret'].label = False

    def clean(self):
        cleaned_data = super(CentreFormationForm, self).clean()
        telephone = cleaned_data.get('telephone')
        siret = cleaned_data.get('siret')

        if telephone == '':
            cleaned_data['telephone'] = None
        if siret == '':
            cleaned_data['siret'] = 'Non renseigné'
        return cleaned_data

    class Meta:
        model = CentreFormation
        fields = ['nom', 'adresse', 'ville',
                  'code_postal', 'telephone', 'siret',
                  'rgpd_generate_conventions']


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Mot de Passe'
        })
    )


class PasswordForgotForm(forms.Form):
    username = forms.CharField(
        label='Enail',
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        })
    )


class PasswordResetForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nouveau mot de Passe'
        })
    )
