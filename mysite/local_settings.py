import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'django-insecure-v%1u%^^o#7=m53&#i#e9+_mvsiil3!qzr)yx#k*an1x0k*lj#-'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.path.join(BASE_DIR, 'db.postgresql'),
    }
}

DEBUG = True
