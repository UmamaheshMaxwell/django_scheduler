import os 
import environ

env=environ.Env()

JSON_KEY_FILE_PATH = os.environ.get('JSON_KEY_FILE_PATH')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["https://django-scheduler-3imv474m7a-uc.a.run.app"]

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8080',  # for localhost (Developlemt)
    'https://django-scheduler-3imv474m7a-uc.a.run.app'
]