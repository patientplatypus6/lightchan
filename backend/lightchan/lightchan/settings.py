"""
Django settings for lightchan project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
from corsheaders.defaults import default_headers
from pathlib import Path
import os
import environ

env = environ.Env()
environ.Env.read_env()
RECAPTCHA_KEY = env("RECAPTCHA_KEY")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2i205g5(5%zeh7vqj6#&)3z8f$2rv#x-x7sf!y)la=#o9&7bdr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = [
#    'www.lightchan.org',
#    'https://www.lightchan.org',
#    'www.lightchan.org/*',
#    'lightchan.org',
#    'lightchan.org/*', 
#    '164.92.157.124'
#]

#ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '164.92.157.124', 'lightchan.org', 'lightchan.org/*', 'www.lightchan.org', 'www.lightchan.org/*']

ALLOWED_HOSTS = ['*']

# Application definition
DATA_UPLOAD_MAX_MEMORY_SIZE = 26214400

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lightone', 
    'corsheaders'
]

SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware', 
    'lightone.middleware.every_request'
]

CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_ALLOW_ALL= True

CORS_ALLOWED_ORIGIN_REGEXES = [
    r".*",
]

CORS_ALLOWED_ORIGINS = [
    "https://domain.com",
    "https://api.domain.com",
    "http://localhost:8080",
    "http://127.0.0.1:9000", 
    "http://localhost:3000",  
    "http://*", 
    "http://www.lightchan.org",
    "https://www.lightchan.org", 
    "https://www.lightchan.org/*"
]

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'access-control-allow-origin',
    'x-requested-with'
]

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT'
]

CSRF_TRUSTED_ORIGINS = [
    "https://*", 
    "http://localhost:3000", 
    "http://*", 
    "https://www.lightchan.org/*",
    "http://www.lightchan.org"
]

ROOT_URLCONF = 'lightchan.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'lightchan.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'lightchan',
       'USER': 'pixel',
       'PASSWORD': 'stardust',
       'HOST': 'db',
       'PORT': '5432'
   }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# STATIC_URL = '/static/'
STATIC_URL = '/static/'
STATICFILES_DIRS = (str(BASE_DIR.joinpath('static')),) # new

MEDIA_URL = '/media/'
# MEDIA_ROOT =(str(BASE_DIR.joinpath('media'))) # new
MEDIA_ROOT = os.path.join(BASE_DIR, '/media/')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
