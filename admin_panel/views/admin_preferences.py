from django.shortcuts import render
from consult_panel.models import *
from django.contrib.auth.decorators import permission_required
from document_generator.models import *


def index(request):
    #user = Profile.objects.get(user=request.user)
    return render(request, 'admin_preferences_index.html', context={
        'user'          :   request.user,
        'page_title'    :   'Préférences',
        'dg_types'      :   DocumentType.objects.all(),
        'dg_templates'  :   Template.objects.all()
        });