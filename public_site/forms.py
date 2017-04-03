# coding: utf-8

from crispy_forms.helper import FormHelper
from django import forms
from django.contrib.auth.models import User

from consult_panel.models import *


class RegistrationForm(forms.ModelForm):

    username = forms.EmailField(required=True, label="Adresse E-mail :")
    first_name = forms.CharField(required=True, label="Prénom :")
    last_name = forms.CharField(required=True, label="Nom :")
    passwordConfirm = forms.CharField(widget=forms.PasswordInput, label="Confirmation :")
    password = forms.CharField(widget=forms.PasswordInput, label="Mot de passe :")

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.label_class = 'col-sm-3 text-right'
        self.helper.field_class = 'col-sm-8'
        super(RegistrationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'username', 'password', 'passwordConfirm']

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        passwordConfirm = cleaned_data.get('passwordConfirm')

        if password != passwordConfirm:
            msg_password = "Les deux mots de passes ne correspondent pas."
            self.add_error('password', msg_password)
            self.add_error('passwordConfirm', msg_password)
            return cleaned_data

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.email = user.username
        user.is_active = False
        if commit:
            user.save()
        return user

class CentreFormationForm(forms.ModelForm):
    nom = forms.CharField(required=True, label="Nom de l'entreprise:")
    siret = forms.CharField(required=True, label="Numéro de siret :")
    adresse = forms.CharField(required=True, label="Adresse :")
    ville = forms.CharField(required=True, label="Ville :")
    code_postal = forms.CharField(required=True, label="Code Postal :")
    telephone =  forms.CharField(required=True, label="Téléphone :")

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.label_class = 'col-sm-3 text-right'
        self.helper.field_class = 'col-sm-8'
        super(CentreFormationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = CentreFormation
        fields = ['nom', 'siret', 'adresse', 'ville',
                  'code_postal', 'telephone']


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nom'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Mot de Passe'
        })
    )
