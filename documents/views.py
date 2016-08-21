from django.shortcuts import render

from consult_panel.models import *
from admin_panel.forms import *
from admin_panel.user_tests import *
from django.contrib.auth.decorators import user_passes_test


@user_passes_test(is_formateur)
def convention(request, id):
    return render(request, 'view_doc.html', context={
        'doc_url': 'my_url'
    })
