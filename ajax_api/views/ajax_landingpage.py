from django.http import JsonResponse
from mailer.mailer import EmailTemplate
from consult_panel.models import EmailForBeta
"""
    This is the ajax part for the landing page
    @author=mastercraft
"""

def add_email(request):
    if 'email' in request.GET:
        try:
            EmailForBeta.objects.get_or_create(email=request.GET.get('email'))
            EmailTemplate('thanks_subscribe_beta').send([request.GET.get('email')])
            status = "success"
            message = "Vous avez reçu un e-mail de confirmation."
        except:
            status = "error"
            message = "Une erreur est survenu, veuillez réessayer plus tard."
    return JsonResponse({
        "status": status,
        "message": message
    });