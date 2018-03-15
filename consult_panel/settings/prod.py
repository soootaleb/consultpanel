from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'cpanel-prod.cwokdcfhoyig.eu-west-1.rds.amazonaws.com',
        'NAME': 'cpanel',
        'USER': 'dbuser',
        'PASSWORD': 'mastercraft',
        'PORT': '5432'
    }
}