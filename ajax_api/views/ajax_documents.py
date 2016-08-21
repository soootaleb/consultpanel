from django.http import JsonResponse
from documents.models import Convention
from django.contrib.auth.decorators import user_passes_test
from admin_panel.user_tests import is_formateur


@user_passes_test(is_formateur)
def convention_sign(request, id):
    try:
        convention = Convention.objects.get(
            pk=id, session__formation__catalogue__profile__user=request.user)
    except expression as identifier:
        status = "KO"
        message = "La convention demandée n'existe pas pour cet utilisateur"
    else:
        convention.signed_by_formateur = True
        convention.save()
        status = "OK"
        message = "La convention a bien été signée"

    return JsonResponse({
        "model":   "Convention",
        "message":   message
        "status":   status,
        "id":   id,
        "action":   'sign'
    })
