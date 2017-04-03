from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from consult_panel.models import *
from admin_panel.forms import *
from admin_panel.user_tests import *
from django.contrib.auth.decorators import user_passes_test


@user_passes_test(is_formateur)
def convention_show(request, id):
    try:
        convention = Convention.objects.filter(
            pk=id, session__formation__catalogue__profile__user=request.user).distinct()[0]
    except Exception as e:
        return HttpResponseBadRequest()
    else:
        return render(request, 'view_doc.html', context={
            'doc_url': convention.document
        })
