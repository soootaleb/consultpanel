from django.http import JsonResponse
from consult_panel.models import *
from django.contrib.auth.decorators import permission_required

def formations_delete(request, id):
    status = "OK"
    formation = Formation.objects.get(pk=id)
    formation.delete()
    return JsonResponse({
        "model"     :   "Formation",
        "status"    :   status,
        "id"        :   id,
        "action"    :   'delete'
    })
