# -*- encoding: utf-8 -*-
SECRET_KEY = '%(secret_key)s'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '%(db_name)s',
        'USER': '%(db_user)s',
        'PASSWORD': '%(db_password)s',
    }
}
