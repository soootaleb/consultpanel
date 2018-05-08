import jinja2
import os
import re
import io

from base64 import urlsafe_b64decode
from tempfile import NamedTemporaryFile
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

    formateur_sign = None
    formateur_sign_img = None
    if convention.signed_by_formateur and profile.signature_base64:
        formateur_sign_img = NamedTemporaryFile(delete=None, suffix='.png')
        img_blob = urlsafe_b64decode(profile.signature_base64)
        formateur_sign_img.write(img_blob)
        formateur_sign_img.close()

        formateur_sign = InlineImage(doc, formateur_sign_img.name)

    jinja_env = jinja2.Environment(autoescape=True)

    context = {
        'convention': convention,
        'client': convention.client,
        'session': convention.session,
        'profile': profile,
        'centre_formation': profile.centre_formation,
        'inscriptions': inscriptions,
        'formateur_sign': formateur_sign,
    }

    doc.render(context, jinja_env)

    content_type = 'application/vnd.openxmlformats-officedocument'
    content_type += '.wordprocessingml.document'
    response = HttpResponse(content_type=content_type)
    response['Content-Disposition'] = 'attachment; filename={}.docx'.format(
        convention_title
    )

    doc.get_docx().save(response)

    if formateur_sign_img:
        os.unlink(formateur_sign_img.name)

    return response
