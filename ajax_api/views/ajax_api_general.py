from django.http import JsonResponse

def get_entites_count(request):
    return JsonResponse({
        'formations': 10,
        'catalogues': 5,
        'sessions': 0,
        'centres': 19,
        'entreprises': 1,
        'clients': 12
    })