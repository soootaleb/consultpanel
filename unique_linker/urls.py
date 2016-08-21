from django.conf.urls import url
from unique_linker import views

urlpatterns = [
    url(r'^generate/(?P<mail>[0-9a-zA-Z@.]+)', views.debug_generate, name="debug_generate"),
    url(r'^(?P<jeton>[0-9a-zA-Z]+)$', views.index, name='index')
]
