"""
Django settings for devtest project.

Generated by 'django-admin startproject' using Django 3.2.14.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    'channels',
    'app.crm.apps.CrmConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'django_celery_results',
    'django_celery_beat',
    'whitenoise.runserver_nostatic'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ROOT_URLCONF = 'devtest.urls'

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

CELERY_ACCEPT_CONTENT = ['application/json']  
CELERY_TASK_SERIALIZER = 'json'  
CELERY_RESULT_SERIALIZER = 'json'  
CELERY_TIMEZONE = "UTC"


ASGI_APPLICATION = 'devtest.asgi.application'

WSGI_APPLICATION = 'devtest.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Extra places for collectstatic to find static files.
""" STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '../app/crm/static'),
) """


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


from .common import *
import os
import dj_database_url

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG')

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(' ')



# Channels
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': os.environ.get('CHANNEL_LAYERS_BACKEND'),
        'CONFIG': {
            "hosts": [os.environ.get('CHANNEL_LAYERS_CONFIG_HOST', 'redis://127.0.0.1:6379')],
        },
    },
}



CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')
#CELERY_RESULT_BACKEND = 'redis://127.0.0.1'


CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND')
CELERY_BEAT_SCHEDULER = os.environ.get('CELERY_BEAT_SCHEDULER')



# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}