from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('public_site.urls')),
    url(r'^api/', include('public_api.urls')),
    url(r'^ajax/', include('ajax_api.urls')),
    url(r'^master/', include('master_panel.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^consult/', include('admin_panel.urls')),
    #url(r'^client/', include('client_panel.urls')), # See you later, my friend.
]

