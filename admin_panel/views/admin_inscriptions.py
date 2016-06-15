from django.shortcuts import render
from consult_panel.models import *


def inscriptions_index(request):
    return render(request, 'admin_inscriptions_index.html', context={
        'sessions_list': Session.objects.filter(formation__catalogue__profile__user=request.user)
    })
