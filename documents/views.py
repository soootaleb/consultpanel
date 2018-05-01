import jinja2
import os
from django.http import HttpResponse
from documents.models import Convention
from consult_panel.models import Profile, Cours, Inscription
from admin_panel import user_tests
from django.contrib.auth.decorators import user_passes_test
from docxtpl import DocxTemplate


@user_passes_test(user_tests.is_formateur)
def convention_show(request, convention_id):

    convention = Convention.objects.get(pk=convention_id)
    profile = Profile.objects.filter(user=request.user).get()
    cours = Cours.objects.get(session=convention.session)
    inscriptions = Inscription.objects.filter(session=convention.session)

    current_dir = os.path.dirname(os.path.realpath(__file__))
    template_path = os.path.join(current_dir, 'templates', 'convention.docx')

    convention_title = 'Convention {} - {}'.format(
        convention.client.nom,
        cours.get_date_debut()
    )

    jinja_env = jinja2.Environment(autoescape=True)

    doc = DocxTemplate(template_path)
    context = {
        'convention': convention,
        'client': convention.client,
        'session': convention.session,
        'profile': profile,
        'centre_formation': profile.centre_formation,
        'cours': cours,
        'inscriptions': inscriptions,
    }
    doc.render(context, jinja_env)

    content_type = 'application/vnd.openxmlformats-officedocument'
    content_type += '.wordprocessingml.document'
    response = HttpResponse(content_type=content_type)
    response['Content-Disposition'] = 'attachment; filename={}.docx'.format(
        convention_title
    )

    doc.get_docx().save(response)

    return response
