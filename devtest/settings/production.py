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