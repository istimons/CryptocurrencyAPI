import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cryptocurrencytrack.settings')

app = Celery('cryptocurrencytrack')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

