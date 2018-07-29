"""Define settings using values of environment variables."""

from os import getenv
from os.path import join, dirname, abspath

from dotenv import load_dotenv


BASE_DIR = abspath(dirname(__file__))
dotenv_path = join(BASE_DIR, '.env')
load_dotenv(dotenv_path)

if getenv('HEROKU'):
	from .prod import *
else:
	from .dev import *
