"""
Django settings for BoletinAvances project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l^9rs!d0e3(!l+94h4b$!vz8sp3d8!vs6goloi#j8pwmfm^w(s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'jquery',
    'djangoformsetjs',
    'BoletinAvances.apps.login',
    'BoletinAvances.apps.listas',
    'BoletinAvances.apps.contactos',
    'BoletinAvances.apps.boletines',
    'BoletinAvances.apps.avances',
    'BoletinAvances.apps.primerasplanas',
    'BoletinAvances.apps.resumen',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'BoletinAvances.urls'

WSGI_APPLICATION = 'BoletinAvances.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-ES'

TIME_ZONE = 'America/Caracas'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), 'media/'))

MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

TEMPLATE_DIRS = (
     os.path.join(os.path.dirname(__file__), 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = [
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
]

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/'
LOGOUT_URL= '/logout'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

DATE_INPUT_FORMATS = ('%d/%m/%Y')

DJANGO_WYSIWYG_FLAVOR = "ckeditor"
CKEDITOR_UPLOAD_PATH = "archivos_boletin/"
CKEDITOR_JQUERY_URL = 'http://localhost:8000/media/jquery-2.1.1/jquery.min.js'

#Agregar configuraciones del SMTP
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'xxxxxxxx@gmail.com'
EMAIL_HOST_PASSWORD = 'xxxxxxxxxxx'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
