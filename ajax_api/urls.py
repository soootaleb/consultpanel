from django.conf.urls import url

from .views import ajax_api_general,\
    ajax_formations,\
    ajax_catalogues,\
    ajax_sessions,\
    ajax_landingpage, \
    ajax_password

urlpatterns = [
    url(r'^$', ajax_api_general.test),
    url(r'^formations/delete/(?P<id>[0-9]+)$', ajax_formations.formations_delete, name='ajax_formations_delete'),
    url(r'^catalogues/delete/(?P<id>[0-9]+)$', ajax_catalogues.catalogues_delete, name='ajax_catalogues_delete'),
    url(r'^sessions/delete/(?P<id>[0-9]+)$', ajax_sessions.sessions_delete, name='ajax_sessions_delete'),
    url(r'^add/email/for/beta/$', ajax_landingpage.add_email, name='ajax_add_email_for_beta'),
    url(r'^password/reset', ajax_password.reset, name="ajax_password_reset")
]
