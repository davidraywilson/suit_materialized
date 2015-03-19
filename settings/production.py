from .base import *

logging.log(logging.INFO, 'loading settings for ' + __name__)

DEBUG = False
TEMPLATE_DEBUG = False

MANAGERS = ('kellym@millcreeksoftware.biz',)

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'template_project',
        'USER': 'millcreek',
        'PASSWORD': 'jupit999',
        'HOST': '',
        'PORT': '',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/webapp_cache',
        'TIMEOUT': 60,  # 60 seconds
    },
}
