from django.shortcuts import render
from consult_panel.models import *
from django.contrib.auth.decorators import permission_required


@user_passes_test(is_formateur)
def profile_index(request):
    #user = Profile.objects.get(user=request.user)
    return render(request, 'admin_profile_index.html', context={
        'user':   request.user,
        'page_title':   'Mon profile'
    })
