# celery.py

from celery import Celery
from config import Config

app = Celery('tasks', broker=f'redis://{Config.HOST}:{Config.CELERY_PORT}/0',
             backend=f'redis://{Config.HOST}:{Config.CELERY_PORT}/0')

app.conf.task_queues = {
    'download_queue': {
        'exchange': 'download',
        'exchange_type': 'direct',
        'binding_key': 'download',
    },
    'audio_queue': {
        'exchange': 'audio',
        'exchange_type': 'direct',
        'binding_key': 'audio',
    },
    'transcribe_queue': {
        'exchange': 'transcribe',
        'exchange_type': 'direct',
        'binding_key': 'transcribe',
    },
    'generate_subtitle_queue': {
        'exchange': 'generate_subtitle',
        'exchange_type': 'direct',
        'binding_key': 'generate_subtitle',
    },
    'add_subtitle_queue': {
        'exchange': 'add_subtitle',
        'exchange_type': 'direct',
        'binding_key': 'add_subtitle',
    },
}

app.conf.task_routes = {
    'tasks.download_video': {'queue': 'download_queue'},
    'tasks.extract_audio': {'queue': 'audio_queue'},
    'tasks.transcribe': {'queue': 'transcribe_queue'},
    'tasks.generate_subtitle_file': {'queue': 'generate_subtitle_queue'},
    'tasks.add_subtitle_to_video': {'queue': 'add_subtitle_queue'},
}

app.conf.worker_pool = 'threads'
app.conf.worker_concurrency = 4
app.conf.broker_connection_retry_on_startup = True
import tasks