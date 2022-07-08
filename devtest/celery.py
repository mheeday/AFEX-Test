import os
from celery import Celery


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devtest.settings')

app = Celery('devtest')

app.config_from_object('django.conf:settings', namespace='CELERY') 

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Hello from celery')





app.conf.beat_schedule = {
    'database-update-1-hour': {
    'task': 'app.crm.tasks.populatedb',
    'schedule': 10,
    'args': ('yes', ),
    },
}