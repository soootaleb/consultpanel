import jinja2
import os
import tempfile
import base64
import re
import io

from django.http import HttpResponse
from documents.models import Convention
from consult_panel.models import Profile, Inscription
from admin_panel import user_tests
from django.contrib.auth.decorators import user_passes_test
from docxtpl import DocxTemplate, InlineImage
from docx.image.image import Image


@user_passes_test(user_tests.is_formateur)
def convention_show(request, convention_id):

    convention = Convention.objects \
        .select_related('cours') \
        .get(pk=convention_id)
    profile = Profile.objects.filter(user=request.user).get()
    inscriptions = Inscription.objects.filter(
        session=convention.session,
        client=convention.client
    )

    current_dir = os.path.dirname(os.path.realpath(__file__))
    template_path = os.path.join(current_dir, 'templates', 'convention.docx')

    convention_title = 'Convention {} - {}'.format(
        convention.client.nom,
        convention.cours.get_date_debut()
    )

    doc = DocxTemplate(template_path)

    signature = None
    tmp_img_file = None
    if profile.signature_base64:
        tmp_img_file = tempfile.NamedTemporaryFile(delete=None, suffix='.jpg')
        img_blob = base64.urlsafe_b64decode(profile.signature_base64)
        tmp_img_file.write(img_blob)
        tmp_img_file.close()

        signature = InlineImage(doc, tmp_img_file.name)

    jinja_env = jinja2.Environment(autoescape=True)

    context = {
        'convention': convention,
        'client': convention.client,
        'session': convention.session,
        'profile': profile,
        'centre_formation': profile.centre_formation,
        'inscriptions': inscriptions,
        'signature': signature,
    }

    doc.render(context, jinja_env)

    if tmp_img_file:
        os.unlink(tmp_img_file.name)

    content_type = 'application/vnd.openxmlformats-officedocument'
    content_type += '.wordprocessingml.document'
    response = HttpResponse(content_type=content_type)
    response['Content-Disposition'] = 'attachment; filename={}.docx'.format(
        convention_title
    )

    doc.get_docx().save("/Users/quentinbrosse/Desktop/file.docx")

    return response
