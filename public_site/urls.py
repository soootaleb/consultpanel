from django.conf.urls import url
from .forms import RegistrationForm, CentreFormationForm
from .views import public_pages

urlpatterns = [
    url(r'^$', public_pages.public_index, name='public_index'),
    url(r'^index/$', public_pages.public_index, name='public_index'),
    url(r'^login/', public_pages.login, name='login'),
    url(r'^logout/', public_pages.logout, name='logout'),
    url(r'^register/', public_pages.RegistrationWizard.as_view([RegistrationForm, CentreFormationForm]), name='register'),
    url(r'^form/(?P<name>[a-z]+)', public_pages.form),
]
