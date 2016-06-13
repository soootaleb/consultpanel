from django.shortcuts import render
from consult_panel.models import *
from django.contrib.auth.decorators import permission_required
from admin_panel.forms.forms import SessionForm


@user_passes_test(is_formateur)
def documents_index(request):
    return render(request, 'admin_documents_index.html', context={
        'page_title': 'Gestion des documents'
    })
