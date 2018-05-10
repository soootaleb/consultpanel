from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^convention/(?P<convention_id>[0-9]+)$',
        views.convention_show, name='document_convention_show'),
]
