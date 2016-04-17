from consult_panel.models import *
from django.forms import *
from crispy_forms.helper import FormHelper

class FormationForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-10'
        super(FormationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Formation
        fields = ['nom', 'description']
        labels = {
            'nom':'Nom : ',
            'description': 'Description : ',
        }
        
class CatalogueForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-10'
        super(CatalogueForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Catalogue
        fields = ['nom', 'liste_formations']
        labels = {
            'nom': 'Nom : ',
            'liste_formations': 'Liste des formations : ',
        }
        
class SessionForm(ModelForm):
    formation = ModelChoiceField(queryset=Formation.objects.all())
    class Meta:
        model = Session
        fields = ['formation']