from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'NAME': 'cpanel_local.db',
        'ENGINE': 'django.db.backends.sqlite3'
    }
}