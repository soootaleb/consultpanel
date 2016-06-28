from django.shortcuts import render
from consult_panel.models import *
from django.contrib.auth.decorators import user_passes_test
from admin_panel.user_tests import *


@user_passes_test(is_formateur)
def profil_index(request):
    #user = Profile.objects.get(user=request.user)
    return render(request, 'admin_profil_index.html', context={
        'user':   request.user,
        'page_title':   'Mon profil'
    })
