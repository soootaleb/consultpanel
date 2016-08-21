from django.http import JsonResponse


def reset(request):
    return JsonResponse({
        "test": "icule"
    })