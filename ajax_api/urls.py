from django.conf.urls import url, include
from django.contrib import admin

from .views import ajax_api_general, ajax_formations, ajax_catalogues, ajax_catalogues, ajax_sessions, ajax_landingpage

urlpatterns = [
    url(r'^$', ajax_api_general.test),
    url(r'^formations/delete/(?P<id>[0-9]+)$', ajax_formations.formations_delete, name='formations_delete'),
    url(r'^catalogues/delete/(?P<id>[0-9]+)$', ajax_catalogues.catalogues_delete, name='catalogues_delete'),
    url(r'^sessions/delete/(?P<id>[0-9]+)$', ajax_sessions.sessions_delete, name='sessions_delete'),
    url(r'^add/email/for/beta/$', ajax_landingpage.add_email, name='add-email-for-beta'),
]
