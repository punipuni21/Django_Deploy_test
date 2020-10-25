import os

#settings.pyからそのままコピー
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECRET_KEY = '#eynx8vqyj)5(mmv3d&dujk%@ma2--3m@qm&9tz*0o%mo5zpg('
SECRET_KEY = '#eynx8vqyj)5(mmv3d&dujk%@ma2--3m@qm&9tz*0o%mo5zpg('

#settings.pyからそのままコピー
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True #ローカルでDebugできるようになります