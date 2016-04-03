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

from .views import public_pages

urlpatterns = [
    url(r'^$', public_pages.index, name='public_index'),
    url(r'^index/$', public_pages.index, name='public_index'),
    url(r'^login/', public_pages.login, name='login'),
    url(r'^logout/', public_pages.logout, name='logout'),
    url(r'^form/(?P<name>[a-z]+)', public_pages.form),
]

