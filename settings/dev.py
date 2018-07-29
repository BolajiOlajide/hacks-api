from os import getenv
from os.path import join, dirname, abspath
from sys import argv

from dotenv import load_dotenv

# import base settings
from .base import *


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = dirname(dirname(abspath(__file__)))
dotenv_path = join(BASE_DIR, '.env')
load_dotenv(dotenv_path)


ALLOWED_HOSTS.append('proton-dev.com')


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
if 'test' in argv:
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.sqlite3',
			'NAME': join(BASE_DIR, 'test.sqlite3'),
		}
	}
else:
	DATABASES = {
	 'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': getenv('DB_NAME'),
		'USER': getenv('DB_USER'),
		'PASSWORD': getenv('DB_PASS'),
		'HOST': getenv('DB_HOST'),
		'PORT': getenv('DB_PORT'),
		'TEST': {
			'CHARSET': None,
			'COLLATION': None,
			'NAME': join(dirname(__file__), 'test.db'),
			'MIRROR': None
		}
	},
 }
