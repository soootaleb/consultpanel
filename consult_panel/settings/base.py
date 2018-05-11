import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

SECRET_KEY = 'or_9e-x+xji0k8p6f@z02r%v#d8&c*2z+w+46)!s-x!4#y0am6'

DEBUG = False

ALLOWED_HOSTS = ['consultpanel.fr', 'consultpanel.info', 'localhost']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'formtools',
    'admin_panel',
    'client_panel',
    'public_api',
    'ajax_api',
    'master_panel',
    'public_site',
    'consult_panel',
    'crispy_forms',
    'documents',
    'unique_linker',
    'mailer'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'consult_panel.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'consult_panel.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DATABASES_DEFAULT_ENGINE') or 'django.db.backends.postgresql_psycopg2',
        'HOST': os.getenv('DATABASES_DEFAULT_HOST'),
        'NAME': os.getenv('DATABASES_DEFAULT_NAME'),
        'USER': os.getenv('DATABASES_DEFAULT_USER'),
        'PASSWORD': os.getenv('DATABASES_DEFAULT_PASSWORD'),
        'PORT': os.getenv('DATABASES_DEFAULT_PORT'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'fr-FR'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'consult_panel', 'static')
LOGIN_URL = '/login/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'consult_panel', 'medias')
MEDIA_URL = '/medias/'

AUTH_PROFILE_MODULE = 'consult_panel.models.Profile'

EMAIL_BACKEND = os.getenv('EMAIL_BACKEND') or 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')
EMAIL_USE_TLS = True

CRISPY_TEMPLATE_PACK = 'bootstrap4'
