from django.http import JsonResponse
from consult_panel.models import *
from django.contrib.auth.decorators import permission_required

@permission_required('consult_panel.is_admin')

def catalogues_delete(request, id):
    status = "OK"
    catalogue = Catalogue.objects.get(pk=id);
    if(catalogue.is_catalogue_of_user(request.user)) :
        catalogue.delete();
    else :
        status = "KO";
    return JsonResponse({
        "model"     :   "Catalogue",
        "status"    :   status,
        "id"        :   id,
        "action"    :   'delete'
    });
