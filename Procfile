web: daphne -b 0.0.0.0 -p 8001 devstart.asgi:application --settings=devtest.settings.development
chatworker: celery -A devtest worker --loglevel=INFO
scheduler: celery -A devtest beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
