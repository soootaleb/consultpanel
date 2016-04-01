from django.http import JsonResponse
from consult_panel.models import *
from django.contrib.auth.decorators import permission_required

def sessions_delete(request, id):
    status = "OK"
    formation = Session.objects.get(pk=id);
    formation.delete();
    return JsonResponse({
        "model"     :   "Session",
        "status"    :   status,
        "id"        :   id,
        "action"    :   'delete'
    });
