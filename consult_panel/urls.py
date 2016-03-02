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

from .views import common_pages

urlpatterns = [
    url(r'^$', common_pages.index),
    url(r'^api/', include('public_api.urls')),
    url(r'^ajax/', include('ajax_api.urls')),
    url(r'^action/', common_pages.action),
    url(r'^index/', common_pages.index, name='common_index'),
    url(r'^login/', common_pages.login, name='login'),
    url(r'^logout/', common_pages.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^consult/', include('admin_panel.urls')),
    url(r'^client/', include('client_panel.urls')),
    url(r'^form/(?P<name>[a-z]+)', common_pages.form),
]

