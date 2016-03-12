from consult_panel.models import Formation
from django.forms import ModelForm

class FormationForm(ModelForm):
    class Meta:
        model = Formation
        fields = ['name', 'description']