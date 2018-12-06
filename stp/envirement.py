import os

from comm.argument import environment

os.environ.setdefault('env', environment)
ENVIRONMENT = os.environ.get('env')

if ENVIRONMENT not in ['local', 'dev', 'production']:
    raise Exception('env local/dev/prod  env=local python3 manage.py runserver')

if ENVIRONMENT == 'dev':
    module_settings = 'stp.settings.development'
if ENVIRONMENT == 'local':
    module_settings = 'stp.settings.local'
if ENVIRONMENT == 'prod':
    module_settings = 'stp.settings.production'
