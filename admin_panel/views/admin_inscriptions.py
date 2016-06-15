from django.shortcuts import render


def inscriptions_index(request):
    return render(request, 'admin_inscriptions_index.html')
