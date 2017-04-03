from django.conf.urls import url

from .views import client_pages

urlpatterns = [
    url(r'^debug/', client_pages.pages_document_inscriptions, name='client_document_inscriptions'),
]
