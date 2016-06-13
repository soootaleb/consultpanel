from django.conf.urls import url, include

from .views import \
    admin_clients, \
    admin_entreprises, \
    admin_pages, \
    admin_profile, \
    admin_preferences, \
    admin_sessions, \
    admin_formations, \
    admin_catalogues, \
    admin_documents, \
    admin_formateurs
urlpatterns = [
    url(r'^$', admin_pages.pages_index, name='admin_index'),
    url(r'^index/$', admin_pages.pages_index, name='admin_index'),

    url(r'^profile/$', admin_profile.profile_index, name='profile_index'),
    url(r'^profile/index/$', admin_profile.profile_index, name='profile_index'),

    url(r'^preferences/$', admin_preferences.preferences_index,
        name='preferences_index'),
    url(r'^preferences/index/$', admin_preferences.preferences_index,
        name='preferences_index'),

    url(r'^documents/$', admin_documents.documents_index, name='documents_index'),
    url(r'^documents/index/$', admin_documents.documents_index,
        name='documents_index'),

    url(r'^sessions/$', admin_sessions.sessions_index, name='sessions_index'),
    url(r'^sessions/index/$', admin_sessions.sessions_index, name='sessions_index'),

    url(r'^sessions/add/$', admin_sessions.sessions_add, name='sessions_add'),
    url(r'^sessions/edit/(?P<id>[0-9]+)$',
        admin_sessions.sessions_edit, name='sessions_edit'),

    url(r'^catalogues/$', admin_catalogues.catalogues_index, name='catalogues_index'),
    url(r'^catalogues/index/$', admin_catalogues.catalogues_index,
        name='catalogues_index'),

    url(r'^catalogues/add/$', admin_catalogues.catalogues_add, name='catalogues_add'),
    url(r'^catalogues/edit/(?P<id>[0-9]+)$',
        admin_catalogues.catalogues_edit, name='catalogues_edit'),

    url(r'^formations/$', admin_formations.formations_index, name='formations_index'),
    url(r'^formations/index/$', admin_formations.formations_index,
        name='formations_index'),
    url(r'^formations/add/$', admin_formations.formations_add, name='formations_add'),
    url(r'^formations/edit/(?P<id>[0-9]+)$',
        admin_formations.formations_edit, name='formations_edit'),

    url(r'^formateurs/$', admin_formateurs.formateurs_index, name='formateurs_index'),
    url(r'^formateurs/index/$', admin_formateurs.formateurs_index,
        name='formateurs_index'),
    url(r'^formateurs/add/$', admin_formateurs.formateurs_add, name='formateurs_add'),
    url(r'^formateurs/edit/(?P<id>[0-9]+)$',
        admin_formateurs.formateurs_edit, name='formateurs_edit'),

    url(r'^entreprises/$', admin_entreprises.entreprises_index,
        name='entreprises_index'),
    url(r'^entreprises/index/$', admin_entreprises.entreprises_index,
        name='entreprises_index'),
    url(r'^entreprises/add/$', admin_entreprises.entreprises_add,
        name='entreprises_add'),
    url(r'^entreprises/edit/(?P<id>[0-9]+)$',
        admin_entreprises.entreprises_edit, name='entreprises_edit'),

    url(r'^clients/$', admin_clients.clients_index, name='clients_index'),
    url(r'^clients/index/$', admin_clients.clients_index, name='clients_index'),
    url(r'^clients/add/$', admin_clients.clients_add, name='clients_add'),
    url(r'^clients/edit/(?P<id>[0-9]+)$',
        admin_clients.clients_edit, name='clients_edit'),

    url(r'^form/(?P<name>[a-z_]+)', admin_pages.form),
]
