# Django settings for poketracer project.
# -*- coding: utf-8 -*-
<<<<<<< HEAD
import os
import socket
from django.utils.translation import ugettext_lazy as _

MEDIA_ROOT_VAR = os.path.dirname(os.path.realpath(__file__))+'/templates'
MEDIA_ROOT_VAR = MEDIA_ROOT_VAR.replace('/poketracer/templates', '/templates')
LOCALE_ROOT_VAR = os.path.dirname(os.path.realpath(__file__))+'/locale'
LOCALE_ROOT_VAR = LOCALE_ROOT_VAR.replace('/poketracer/locale', '/locale/')
=======

import os

HOSTING = 'poketracer' #MUDAR QUANDO ESTIVER NO SERVIDOR DE PRODUCAO OU TESTE EX: http://127.0.0.1:8000/poketracer/home/safari/
DEBUG = True
TEMPLATE_DEBUG = DEBUG
# COLOCAR O CAMINHO ATE O SEU DIRETORIO DE TEMPLATE - CAMINHO COMPLETO

#MEDIA_ROOT_VAR = '/home/edson/Projetos/virtualPoketracer/poketracer/templates'
#MEDIA_ROOT_VAR = '/home/gabriel/Projetos/virtualPoketracer/poketracer/templates'
#MEDIA_ROOT_VAR = '/home/lucaslinux/projetos/poketracer/templates'
MEDIA_ROOT_VAR = os.path.dirname(os.path.realpath(__file__))+'/templates'
MEDIA_ROOT_VAR = MEDIA_ROOT_VAR.replace('/poketracer/templates', '/templates')
>>>>>>> a8c17f46a81f6565aebe88e96638a4306bbaa4c2

ADMINS = (
    # ('celula', 'suporte@celuladigital.com.br'),
)

MANAGERS = ADMINS

<<<<<<< HEAD
EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_HOST_USER = 'social@poketracer.com.br'
EMAIL_HOST_PASSWORD = ''
DEFAULT_FROM_EMAIL = 'PokeTracer <social@poketracer.com.br>'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

dadosServidor = socket.gethostname()

#NA INTERNET PARA RODAR MAIS RAPIDO
if dadosServidor == 'poketracer':
    SERVIDOR = '127.0.0.1'
    DEBUG = False
else:
    DEBUG = True
    SERVIDOR = '23.94.32.93'

TEMPLATE_DEBUG = DEBUG

DATABASES = {'default': {
'ENGINE': 'django.db.backends.mysql',
'NAME': 'poketracer',
'USER': 'root',
'PASSWORD': '',
'HOST': SERVIDOR,
'PORT': '3306',
}} 

#CRIAR O BANCO: CREATE DATABASE poketracer DEFAULT CHARACTER SET latin1 COLLATE latin1_general_ci; USE poketracer;

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '23.94.32.93','poketracer.com', 'www.poketracer.com']
=======
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
>>>>>>> a8c17f46a81f6565aebe88e96638a4306bbaa4c2

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Sao_Paulo'

# Language code for this installation. All  choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html

<<<<<<< HEAD
LANGUAGE_CODE = 'en-us'
LANGUAGE = (
    ('pt-BR', _('Português')),
    ('en-us', _('English')),
    ('es', _('Español')),
)

LOCALE_PATHS = (
    LOCALE_ROOT_VAR,
)

=======
LANGUAGE_CODE = 'pt-br'
LANGUAGE = (

    ('pt-br', u'Portugues'),
    ('en', u'Ingles'),
    ('es', u'Espanhol')

)


>>>>>>> a8c17f46a81f6565aebe88e96638a4306bbaa4c2
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
<<<<<<< HEAD
MEDIA_URL = '/media/'
=======
MEDIA_URL = 'http://127.0.0.1:8000/media/'
>>>>>>> a8c17f46a81f6565aebe88e96638a4306bbaa4c2

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
<<<<<<< HEAD
SECRET_KEY = ''
=======
SECRET_KEY = 'xsaz^-b%ac3h30e4_351xhm6qwve^4r8jbqr%a1=31#ve3w(!6'
>>>>>>> a8c17f46a81f6565aebe88e96638a4306bbaa4c2

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
<<<<<<< HEAD
    'django.middleware.locale.LocaleMiddleware',
=======

    #'django.middleware.locale.localeMiddleware',

>>>>>>> a8c17f46a81f6565aebe88e96638a4306bbaa4c2
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

<<<<<<< HEAD
#AUTENTICACAO http://django-facebook.readthedocs.org/
#FACEBOOK_APP_ID              = ''
#FACEBOOK_API_SECRET          = ''

=======
>>>>>>> a8c17f46a81f6565aebe88e96638a4306bbaa4c2
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

<<<<<<< HEAD
#AUTHENTICATION_BACKENDS = (
    #'django_facebook.auth_backends.FacebookBackend',
    #'django.contrib.auth.backends.ModelBackend',
#)

#AUTH_USER_MODEL = 'django_facebook.FacebookCustomUser'

=======
>>>>>>> a8c17f46a81f6565aebe88e96638a4306bbaa4c2
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
