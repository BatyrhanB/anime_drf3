import os
from celery import Celery
import logging
from django.conf import settings

#you can use these celery settings for your project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
 
app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task
def divide(x, y):
    import time
    time.sleep(5)
    return x / y

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
