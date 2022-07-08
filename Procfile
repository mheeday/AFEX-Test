web: daphne devstart.asgi:application --port $PORT --bind 0.0.0.0 -v2
chatworker: celery -A devtest worker -B devtest beat --loglevel=INFO -v2
