from django.shortcuts import render
from consult_panel.models import *
from django.contrib.auth.decorators import permission_required

@permission_required('consult_panel.is_admin')
def sessions_index(request):
    return render(request, 'admin_sessions_index.html', context={'page_title' : 'Gestion des sessions'});