from django.shortcuts import render
from consult_panel.models import *
from consult_panel.settings import *
from django.contrib.auth.decorators import user_passes_test
from document_generator.models import *
from document_generator.generators import ConventionGenerator
from admin_panel.forms import FileForm
from admin_panel.user_tests import *

import os


@user_passes_test(is_formateur)
def preferences_index(request):
    generator = ConventionGenerator(request.user)
    profile = Profile.objects.get(user=request.user)
    profile_folder = profile.get_medias_directory()
    files = os.listdir(profile_folder)
    pdf_ones = [x for x in files if x[-4:] == '.pdf']
    return render(request, 'admin_preferences_index.html', context={
        'user':   request.user,
        'page_title':   'Préférences',
        'form': FileForm(),
        'dg_types':   DocumentType.objects.all(),
        'dg_templates': pdf_ones,
        'generated_file': generator.generate('myfile.html').with_context({
            'my_message': 'This is my message',
            'document_title': 'Convention de stage',
            'document_description': 'DocumentGenerator demonstration'
        }).as_html()
    })
