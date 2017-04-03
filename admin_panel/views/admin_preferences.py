from django.shortcuts import render
from consult_panel.models import *
from consult_panel.settings import *
from django.contrib.auth.decorators import user_passes_test
from documents.models import *
from documents.generators import ConventionGenerator
from admin_panel.forms import FileForm
from admin_panel.user_tests import *
from consult_panel.settings import MEDIA_ROOT
import os


@user_passes_test(is_formateur)
def preferences_index(request, tab):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'admin_preferences_index.html', context={
        'user':   request.user,
        'page_title':   'Préférences',
        'form': FileForm(),
        'dg_types':   DocumentType.objects.all(),
        'dg_templates': Template.objects.filter(profile=profile),
        'active_tab': tab if tab in ['docs', 'add', 'test'] else 'docs'
    })
