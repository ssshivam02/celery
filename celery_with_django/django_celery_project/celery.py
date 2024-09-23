from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings
from django_celery_beat.models import PeriodicTask

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_project.settings')

app = Celery('django_celery_project')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings, namespace = 'CELERY')

# here we add celery Beat settings
app.conf.beat_schedule={
    'senf-mail-everyday-at-8':{
        'task': 'send_mail_app.tasks.send_mail_func',
        'schedule': crontab(hour=8, minute=0),
        # args :(1,)
    }
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')  # Print the request object
    
