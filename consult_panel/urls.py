from django.conf import settings
from django.contrib import admin
from django.conf.urls import url, include, patterns
from django.conf.urls.static import static

handler404 = 'public_site.views.public_errors.error404'
handler500 = 'public_site.views.public_errors.error500'

urlpatterns = [
    url(r'^', include('public_site.urls')),
    url(r'^api/', include('public_api.urls')),
    url(r'^ajax/', include('ajax_api.urls')),
    url(r'^master/', include('master_panel.urls')),
    url(r'^client/', include('client_panel.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^consult/', include('admin_panel.urls')),
    url(r'^u/', include('unique_linker.urls')),
    url(r'docs/', include('documents.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_ROOT, document_root=settings.STATIC_ROOT)
