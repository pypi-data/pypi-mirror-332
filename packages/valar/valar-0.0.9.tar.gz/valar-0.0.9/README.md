valar for morghulis

# settings
```python
from pathlib import Path

""" Compulsory settings """
DEBUG = True
BASE_DIR = Path(__file__).resolve().parent.parent
BASE_APP = str(BASE_DIR.name)
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

""" Minimized compulsory settings """

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

INSTALLED_APPS = [
    'django.contrib.sessions',
    "corsheaders",
    'channels',
    'valar.dao'
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'valar.Middleware'
]

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
ROOT_URLCONF = "%s.urls" % BASE_APP
ASGI_APPLICATION = "%s.asgi.application" % BASE_APP
VALAR_CHANNEL_HANDLER_MAPPING = "%s.urls.channel_handler_mapping" % BASE_APP

""" Optional settings """
# ALLOWED_HOSTS = ['*']
# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'Asia/Shanghai'
# USE_I18N = True
# USE_TZ = False
# SESSION_SAVE_EVERY_REQUEST = True
# SESSION_COOKIE_AGE = 60 * 60
# FILE_UPLOAD_MAX_MEMORY_SIZE = 1024 * 1024 * 100
# DATA_UPLOAD_MAX_MEMORY_SIZE = 1024 * 1024 * 100
```

# root urls





# prepare
```sh
python -m pip install --upgrade pip
```
```sh
pip install --upgrade build
```
```sh
pip install twine
```

# publish
```sh
rm -r dist
```
```sh
python -m build
```
```sh
twine check dist/*
```
```sh
twine upload dist/*
```