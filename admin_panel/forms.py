from consult_panel.models import *
from django.forms import *

class FormationForm(ModelForm):
    class Meta:
        model = Formation
        fields = ['nom', 'description']
        
class CatalogueForm(ModelForm):
    class Meta:
        model = Catalogue
        fields = ['nom', 'liste_formations']
        
class SessionForm(ModelForm):
    formation = ModelChoiceField(queryset=Formation.objects.all())
    class Meta:
        model = Session
        fields = ['formation']