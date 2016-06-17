from django import forms
from crispy_forms.helper import FormHelper
from .models import *


class ProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-10'
        super(ProfileForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Profile
        fields = ['user', 'liste_catalogues']
