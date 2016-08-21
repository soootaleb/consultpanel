from django.http import JsonResponse
from documents.models import Convention
from django.contrib.auth.decorators import user_passes_test
from admin_panel.user_tests import is_formateur


@user_passes_test(is_formateur)
def convention_sign(request, id):
    try:
        convention = Convention.objects.filter(
            pk=id, session__formation__catalogue__profile__user=request.user).distinct()[0]
    except Exception as e:
        status = "KO"
        message = "La convention demandée n'existe pas pour cet utilisateur"
    else:
        convention.signed_by_formateur = True
        convention.save()
        status = "OK"
        message = "La convention a bien été signée"

    return JsonResponse({
        "model":   "Convention",
        "message":   message,
        "status":   status,
        "id":   id,
        "action":   'sign'
    })


@user_passes_test(is_formateur)
def convention_send(request, id):
    try:
        convention = Convention.objects.filter(
            pk=id, session__formation__catalogue__profile__user=request.user).distinct()[0]
    except Exception as e:
        status = "KO"
        message = "La convention demandée n'existe pas pour cet utilisateur"
    else:
        # ToDo :
        # - Create uLink
        # - Send mail with uLink
        # We won't need to do anything around document here
        # It'll be generated on GET request to show it
        status = "OK"
        message = "La convention a bien été envoyée au client"

    return JsonResponse({
        "model":   "Convention",
        "message":   message,
        "status":   status,
        "id":   id,
        "action":   'send'
    })
