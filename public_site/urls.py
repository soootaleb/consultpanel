from django.conf.urls import url

from .forms import RegistrationForm, CentreFormationForm
from .views import public_pages

urlpatterns = [
    url(r'^$', public_pages.public_index, name='public_root'),
    url(r'^index/$', public_pages.public_index, name='public_index'),
    url(r'^login/', public_pages.login, name='public_login'),
    url(r'^logout/', public_pages.logout, name='public_logout'),
    url(r'^register/', public_pages.RegistrationWizard.as_view([RegistrationForm, CentreFormationForm]), name='public_register'),
    url(r'^forgot-password', public_pages.forgot_password, name="public_forgot_password"),
    url(r'^form/(?P<name>[a-z_]+)', public_pages.form, name="public_form"),
]
