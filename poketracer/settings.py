# Django settings for poketracer project.
# -*- coding: utf-8 -*-

import os

HOSTING = '' #MUDAR QUANDO ESTIVER NO SERVIDOR DE PRODUCAO OU TESTE EX: http://127.0.0.1:8000/poketracer/home/safari/
DEBUG = True
TEMPLATE_DEBUG = DEBUG
# COLOCAR O CAMINHO ATE O SEU DIRETORIO DE TEMPLATE - CAMINHO COMPLETO

#MEDIA_ROOT_VAR = '/home/edson/Projetos/virtualPoketracer/poketracer/templates'
#MEDIA_ROOT_VAR = '/home/gabriel/Projetos/virtualPoketracer/poketracer/templates'
#MEDIA_ROOT_VAR = '/home/lucaslinux/projetos/poketracer/templates'
MEDIA_ROOT_VAR = os.path.dirname(os.path.realpath(__file__))+'/templates'
MEDIA_ROOT_VAR = MEDIA_ROOT_VAR.replace('/poketracer/templates', '/templates')

ADMINS = (
    # ('celula', 'suporte@celuladigital.com.br'),
)

MANAGERS = ADMINS

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'mail@poketracer.com.br'
EMAIL_HOST_PASSWORD = 'ADMIN1212'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'PokeTracer <mail@poketracer.com.br>'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': 'bancoTeste.sqlite3',
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'celuladigital15', 
        'USER': 'celuladigital15',
        'PASSWORD': 'CDS1005',
        'HOST': '201.76.55.146',
        'PORT': '3306',
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Sao_Paulo'

# Language code for this installation. All  choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html

LANGUAGE_CODE = 'pt-br'
LANGUAGE = (

    ('pt-br', u'Portugues'),
    ('en', u'Ingles'),
    ('es', u'Espanhol')

)


SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = MEDIA_ROOT_VAR

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = 'http://127.0.0.1:8000/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'xsaz^-b%ac3h30e4_351xhm6qwve^4r8jbqr%a1=31#ve3w(!6'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',

    #'django.middleware.locale.localeMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'poketracer.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'poketracer.wsgi.application'

TEMPLATE_DIRS = (
    MEDIA_ROOT_VAR
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pessoas',
    'pokemons',
)

#PARA FUNCIONAR A SESSAO DIRETAMENTE NO TEMPLATE
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    )

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
