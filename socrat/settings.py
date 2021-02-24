from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4ojbv9$u&!##&)!0u)lab=jqbhhow4so18!4g#+yr$=7#o0n6='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #local apps
    'web',

    #3rd party apps
    'flat',
    'imagekit',
    'ckeditor',
    'ckeditor_uploader',
    'mathfilters',
]



CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {

    'default': {
        'toolbar': 'Custom',
        'width': '100%',
        'toolbar_Custom': [
            ['Styles', 'Format', 'Bold', 'Italic', 'Underline', 'Strike', 'justifycenter', 'SpellChecker', 'Undo',
             'Redo', 'cleanup'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
             'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl', 'Language'],
            ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates'],
            ['Link', 'Unlink', 'Anchor'],
            ['TextColor', 'BGColor'],
            ['Smiley', 'SpecialChar'],
            ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates', 'RemoveFormat'],
            ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']

        ],
    },
    'special': {
        'toolbar': 'Special',
        'toolbar_Special': [
            ['Bold'],
        ],
    }
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'socrat.urls'

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

WSGI_APPLICATION = 'socrat.wsgi.application'


DATABASES = {
   # 'default': {
   #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
   #     'NAME': 'SocratDataBase',
   #     'USER': 'postgres',
   #     'PASSWORD': 'admin',
   #     'HOST': '127.0.0.1',
   #     'PORT': '5432',
   # }
     'default': {
          'ENGINE': 'django.db.backends.sqlite3',
	  'NAME': 'mydatabase'
     }
}


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# STATICFILES_DIRS = [
#     BASE_DIR / "static",
#     '/var/www/static/',
# ]

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

MEDIA_URL = '/media/'
MEDIA_DIR = 'media/'

STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATIC_URL = '/static/'
STATIC_DIR = 'static/'

PDF_ROOT = os.path.join(BASE_DIR, "static")
