import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv('.env'))

class Config:
    DEBUG = True
    HOST = os.environ.get('HOST') or "localhost"
    CELERY_PORT = int(os.environ.get('CELERY_PORT')) or 6379
    FASTAPI_PORT = int(os.environ.get('FASTAPI_PORT')) or 8000
    MONGO_PORT = int(os.environ.get('MONGO_PORT')) or 27017