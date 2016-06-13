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

PDF_FILE = os.path.join(MEDIA_ROOT, 'admin_documents', 'convention.pdf')


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


def update_template(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="%s"' % PDF_FILE

    buffer = BytesIO()

    # Create the PDF object, using the BytesIO object as its "file."
    p = canvas.Canvas(PDF_FILE)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly.
    p.showPage()
    p.save()

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

    return render(request, 'admin_preferences_update_template.html', context={
        'page_title': 'Modification de document'
    })
