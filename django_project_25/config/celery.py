import os
import logging

from celery import Celery
from celery.schedules import crontab
from django.conf import settings
from django.apps import apps


from logging import Logger

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

PRIORITY_HIGH = 0
PRIORITY_NORMAL = 1
PRIORITY_LOW = 2

LOCALLY_BLOCKING = False


class CeleryConfig:
    broker_url = settings.REDIS_LOCATION
    result_backend = settings.REDIS_LOCATION
    timezone = settings.TIME_ZONE
    task_ignore_result = True
    task_remote_traceback = True
    worker_max_task_per_child = 300
    worker_lost_waite = 120
    task_soft_time_limit = 60 * 4
    task_time_limit = 60 * 4 * 4
    beat_schedule = None
    task_default_queue = 'default'
    broker_transport_options = {
        'priority_steps': list(range(10)),
        'visibility_timeout': 60 * 60 * 24,
    }
    task_publish_retry = True
    task_publish_retry_policy = {
        'max_retries': 2,
        'interval_start': 0.2,
        'interval_step': 0.9,
        'interval_max': 2,
    }
    task_always_eager = LOCALLY_BLOCKING
    task_eager_propagates = LOCALLY_BLOCKING


CeleryConfig.beat_schedule = {
    'show_test_task': {
        'task': 'show_test_task',
        'schedule': crontab(minute='*'),
        'options': {
            'priority': PRIORITY_HIGH,
        },
    },
}

app = Celery('my_celery')
# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object(CeleryConfig)
# Load task modules from all registered Django apps.
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])


class ErrorLoggingTask(app.Task):
    def on_failure(self, exc, task_id, args, kwargs, e_info):
        message = (
            f'Celery task exception.'
            f'Task {self.name} ({task_id})'
            f'Exception: {exc.__class__.__name__}.'
        )

        if args:
            message = f'(message) Args: {",".join((str(a) for a in args))}'

        if kwargs:
            t_kwargs = ','.join(f'{k}:{v}' for k, v in kwargs.items())
            message = f'{message} Kwargs: {t_kwargs}'

        message = f'{message}. Info: {e_info}'
        logging.error(message, exc_info=exc)
        Logger.error(message, exc_info=exc)
