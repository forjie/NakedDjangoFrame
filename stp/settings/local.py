from stp.settings.base import *

DEBUG = True

INTERNAL_IPS = [
    '*',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'stp',
        'USER': 'root',
        'PASSWORD': '123',
        'HOST': '127.0.0.1',  # Or an IP Address that your DB is hosted on
        'PORT': '3306',
        'CHARSET': 'utf8mb4',
        'COLLATION': 'utf8mb4_general_ci',
        'TEST': {
            'NAME': 'test_mei_saas',
            'CHARSET': 'utf8mb4',
            'COLLATION': 'utf8mb4_bin',
        },
        'OPTIONS': {
            'charset': 'utf8mb4',
            "init_command": "SET foreign_key_checks = 0;",
        },
    },
}

DB_FILE_NAME = os.path.join(os.path.join(os.path.dirname(BASE_DIR), "sql"), "init_db.sql")
INSTALLED_APPS.append('commands')
