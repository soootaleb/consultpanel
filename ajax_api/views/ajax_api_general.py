from django.http import JsonResponse
from consult_panel.models import *

def get_entites_count(request):
    return JsonResponse({
        'sessions': Session.objects.filter(formation__catalogue__profile__user=request.user).distinct().count(),
        'formations': Formation.objects.filter(catalogue__profile__user=request.user).distinct().count(),
        'clients': Client.objects.filter(catalogue__profile__user=request.user).distinct().count(),
        'catalogues': Catalogue.objects.filter(profile__user=request.user).exclude(nom='main').distinct().count(),
        'entreprises': Profile.objects.get(user=request.user).liste_entreprises.count(),
        'centres': Localisation.objects.filter(profile__user=request.user).distinct().count()
    })