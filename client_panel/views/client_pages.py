from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'client_pages_index.html', context={
        'page_title'        :   "Bienvenue sur votre espace client"
    })