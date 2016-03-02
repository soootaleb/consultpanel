from django.shortcuts import render

def test(request):
    return render(request, 'ajax_api_container.html', context={'response':"Hey this is a test"});
