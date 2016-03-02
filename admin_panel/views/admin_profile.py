from django.shortcuts import render
from consult_panel.models import *
from django.contrib.auth.decorators import permission_required

@permission_required('consult_panel.is_consultant')
def index(request):
    #user = Profile.objects.get(user=request.user)
    return render(request, 'admin_profile_index.html', context={'user':user});