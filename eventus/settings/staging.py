from .base import *

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ddr7vsme368kpk',
        'USER': 'uqtcqbikbmraoo',
        'PASSWORD': '0ySz9pkrhDuyRBlwNo2ygln6gi',
        'HOST': 'ec2-54-204-41-175.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')