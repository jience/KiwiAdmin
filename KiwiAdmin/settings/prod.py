# settings/prod.py
from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rikvaw31h3_41l022!!b!zby4ny_e&bkr2*2rg@3qm4lxeup4&' or os.getenv('SECRET_KEY')


DEBUG = False

ALLOWED_HOSTS = ['kiwipos.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Kiwi',
        'USER': 'root',
        'PASSWORD': 'root123456',
        'HOST': 'kiwipos.com',
        'PORT': 3306,
    }
}
