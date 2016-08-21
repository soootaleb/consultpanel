from django.conf.urls import url, include, patterns
from django.conf.urls.static import static
from django.contrib import admin

from consult_panel.settings import MEDIA_ROOT, MEDIA_URL, STATIC_ROOT, DEBUG

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

] + static(MEDIA_URL, document_root=MEDIA_ROOT)

# To make server serve static files while DEBUG = False
# Done automaticaly if DEBUG is True)
if DEBUG is False:
    urlpatterns += patterns('',
                            url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
                                {'document_root': STATIC_ROOT}),
                            )
