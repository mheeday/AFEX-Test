web: daphne devstart.asgi:application --port $port --bind 0.0.0.0 --settings=devtest.settings.development
chatworker: celery -A devtest worker -B devtest beat --loglevel=INFO
