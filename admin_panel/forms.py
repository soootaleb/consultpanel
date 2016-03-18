from consult_panel.models import *
from django.forms import ModelForm

class FormationForm(ModelForm):
    class Meta:
        model = Formation
        fields = ['name', 'description']
        
class CatalogueForm(ModelForm):
    class Meta:
        model = Catalogue
        fields = ['name', 'description', 'liste_formations']