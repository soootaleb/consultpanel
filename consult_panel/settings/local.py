from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': '0.0.0.0',
        'PORT': 5432
    }
}

UNIQUE_LINKER_BASE_URL = "http://localhost:8000"
CONSOLE_MAILER = True