from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-61vr#!3)f^effz!0n3_yi4pdpxzymmxrxi(!9rxf&p(hn1ujx)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Channels
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}

CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
#CELERY_RESULT_BACKEND = 'redis://127.0.0.1'

CELERY_RESULT_BACKEND = 'django-db'
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'





# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

""" DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
} """

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': 'afextestdb',
       'USER': 'postgres',
       'PASSWORD': 'postgres',
       'HOST': '127.0.0.1',
       'PORT': '5432',
   }
}
