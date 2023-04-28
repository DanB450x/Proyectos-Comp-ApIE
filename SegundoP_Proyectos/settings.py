# settings.py

...

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'HELADPS',
        'USER': 'postgres',
        'PASSWORD': 'proyectos',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

...

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'heladeria',
]

...