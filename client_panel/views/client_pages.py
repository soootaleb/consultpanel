from django.shortcuts import render


def pages_document_inscriptions(request):
    return render(request, 'client_document_inscriptions.html', context={})
