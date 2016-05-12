from django.shortcuts import render
from consult_panel.models import *
from django.contrib.auth.decorators import permission_required
from admin_panel.forms.forms import ProfileForm


def clients_index(request):
    return render(request, 'admin_clients_index.html', context={
        'page_title'        : 'Gestion des clients',
        'clients_list'     : Profile.objects.all()
        });
        
def clients_add(request):
    return render(request, 'admin_clients_add.html', {
        'page_title'        : 'Ajouter un client',
        'form'              : ProfileForm()
    });
    
def clients_edit(request, id):
    return render(request, 'admin_clients_edit.html', {
        'page_title'        : 'Editer un client',
        'form'              : ProfileForm(instance=Profile.objects.get(pk=id))
    });
    