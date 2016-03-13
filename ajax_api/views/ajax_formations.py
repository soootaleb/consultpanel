from django.http import JsonResponse
from consult_panel.models import *
from django.contrib.auth.decorators import permission_required

@permission_required('consult_panel.is_admin')

def formations_delete(request, id):
    status = "OK"
    formation = Formation.objects.get(pk=id);
    if(formation.is_formation_of_user(request.user)) :
        formation.delete();
    else :
        status = "KO";
    return JsonResponse({
        "status"    :   status,
        "id"        :   id,
        "action"    :   'delete'
    });
