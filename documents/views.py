from django.http import HttpResponse
from consult_panel.models import *
from admin_panel.user_tests import *
from django.template.loader import render_to_string
from django.contrib.auth.decorators import user_passes_test

import pdfkit

@user_passes_test(is_formateur)
def convention_show(request, id):

    html  = render_to_string('convention.html', {
        'convention': Convention.objects.get(pk=id)
    })

    pdf = pdfkit.PDFKit(html, 'string', options={
        'dpi': 380
    }).to_pdf()

    return HttpResponse(pdf, content_type='application/pdf')
