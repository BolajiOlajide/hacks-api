# Parse database configuration from $DATABASE_URL
import dj_database_url

# import base settings
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

DEBUG = False

DATABASES = {
	'default': dj_database_url.config()
}
