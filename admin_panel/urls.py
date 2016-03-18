"""consult_panel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from .views import admin_pages, admin_profile, admin_sessions, admin_formations, admin_catalogues

urlpatterns = [
    url(r'^$', admin_pages.index, name='admin_index'),
    url(r'^index/$', admin_pages.index, name='admin_index'),
    url(r'^profile/$', admin_profile.index, name='profile_index'),
    url(r'^sessions/$', admin_sessions.sessions_index, name='sessions_index'),
    url(r'^sessions/index/$', admin_sessions.sessions_index, name='sessions_index'),
    url(r'^catalogues/$', admin_catalogues.catalogues_index, name='catalogues_index'),
    url(r'^catalogues/index/$', admin_catalogues.catalogues_index, name='catalogues_index'),
    url(r'^catalogues/add/$', admin_catalogues.catalogues_add, name='catalogues_add'),
    url(r'^catalogues/edit/(?P<id>[0-9]+)$', admin_catalogues.catalogues_edit, name='catalogues_edit'),
    url(r'^formations/$', admin_formations.formations_index, name='formations_index'),
    url(r'^formations/index/$', admin_formations.formations_index, name='formations_index'),
    url(r'^formations/add/$', admin_formations.formations_add, name='formations_add'),
    url(r'^formations/edit/(?P<id>[0-9]+)$', admin_formations.formations_edit, name='formations_edit'),
    url(r'^form/(?P<name>[a-z_]+)', admin_pages.form),
]
