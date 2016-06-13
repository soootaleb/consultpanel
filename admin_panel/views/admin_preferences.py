from django.shortcuts import render
from consult_panel.models import *
from consult_panel.settings import *
from django.contrib.auth.decorators import permission_required
from document_generator.models import *
from admin_panel.forms.forms import FileForm

from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse

import os


def preferences_index(request):
    #user = Profile.objects.get(user=request.user)
    files = os.listdir(os.path.join(MEDIA_ROOT, 'admin_documents'))
    pdf_ones = [x for x in files if x[-4:] == '.pdf']
    return render(request, 'admin_preferences_index.html', context={
        'user':   request.user,
        'page_title':   'Préférences',
        'form': FileForm(),
        'dg_types':   DocumentType.objects.all(),
        'dg_templates': pdf_ones
        #'dg_templates':   Template.objects.all()
    })
