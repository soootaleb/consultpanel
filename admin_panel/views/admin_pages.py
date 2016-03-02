from django.shortcuts import render
from consult_panel.models import *
from django.contrib.auth.decorators import permission_required

@permission_required('consult_panel.is_admin')
def index(request):
    
    context = {
        'page_title'        :   'Dashboard',
        'formation_list'    :   Formation.objects.all(),
    }
    
    return render(request, 'admin_pages_index.html', context=context);

# Getting common forms routed here. Process is done in common_forms.py
def form(request, name):
    from . import admin_forms
    if request.method == 'POST' :
        response = getattr(admin_forms, name)(request)
        return response if response is not None else redirect('consult/')
    else :
        messages.warning('Oops, vous vous êtes perdu...')
        return redirect('consult/')   
    
def about(request):
    pass;

def contact(request):
    pass;