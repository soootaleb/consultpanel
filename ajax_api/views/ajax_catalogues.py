from django.http import JsonResponse

from consult_panel.models import *


def catalogues_delete(request, id):
    status = "OK"
    catalogue = Catalogue.objects.get(pk=id);
    return JsonResponse({
        "model"     :   "Catalogue",
        "status"    :   status,
        "id"        :   id,
        "action"    :   'delete'
    })
