web: daphne devtest.asgi:application --port $PORT --bind 0.0.0.0 -v2
chatworker: celery -A devtest worker -B --loglevel=INFO -v2
