from django.shortcuts import render


def error404(request):
    return render(request, 'public_pages_errors_404.html', status=404)


def error500(request):
    return render(request, 'public_pages_errors_500.html', status=500)
