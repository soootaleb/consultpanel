# coding: utf-8

from consult_panel.models import *
from django.forms import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.models import User

class RegistrationForm(ModelForm):

    first_name = CharField(required=True)
    last_name = CharField(required=True)
    passwordConfirm = CharField(widget=PasswordInput)
    password = CharField(widget=PasswordInput)

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.label_class = 'col-sm-3 text-right'
        self.helper.field_class = 'col-sm-8'
        super(RegistrationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'passwordConfirm']
        labels = {
            'first_name': 'Prénom :',
            'last_name': 'Nom :',
            'username': 'Adresse E-mail :',
            'email': 'Confirmation :',
            'password': 'Mot de passe :',
            'passwordConfirm': 'Confirmation :',

        }

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        passwordConfirm = cleaned_data.get('passwordConfirm')
        email = cleaned_data.get('email')
        username = cleaned_data.get('username')


        if email != username :
            msg_email = "Les deux emails ne correspondent pas."
            self.add_error('email', msg_email)
            self.add_error('username', msg_email)
            return cleaned_data


        if password != passwordConfirm:
            msg_password = "Les deux mots de passes ne correspondent pas."
            self.add_error('password', msg_password)
            self.add_error('passwordConfirm', msg_password)
            return cleaned_data



    def save(self, commit=True):
        """
        Processus de creation d'un compte utilisateur
        """
        return self.save()


class ProfileForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-10'
        super(ProfileForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Profile
        fields = ['user', 'liste_entreprises', 'liste_catalogues']
