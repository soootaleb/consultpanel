from django.shortcuts import render
from consult_panel.models import *
from django.contrib.auth.decorators import permission_required
from admin_panel.forms import SessionForm


def documents_index(request):
    return render(request, 'admin_documents_index.html');
    