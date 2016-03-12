from django.shortcuts import render

def formations_delete(request, id):
    return render(request, 'ajax_api_container.html', {'response' : '{"id":'+id+'}'});