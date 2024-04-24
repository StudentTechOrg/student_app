

import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))




# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%*tf6x$q07onvy^ge1zc7*$l+(44buv8vtd6wkx7)1e$oujm1b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ["*"]

# MEDIA_URL="/media/"
# MEDIA_ROOT=os.path.join(BASE_DIR,"media")

# STATIC_URL="/static/"
# STATIC_ROOT=os.path.join(BASE_DIR,"static")

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




DEFAULT_FILE_STORAGE = 'student_system.azure_storage.AzureMediaStorage'
STATICFILES_STORAGE = 'student_system.azure_storage.AzureStaticStorage'

AZURE_ACCOUNT_NAME = 'c2087665'
AZURE_ACCOUNT_KEY = 'FXyZTY5wiUX3/Np/ugZuGJqwhrlAYMzjmmuJk3EHQs8KrGqp7RHmpB0h6XnXMMLRPKkRnMQyt5pp+AStWHutmA=='
AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'

STATIC_URL = f'https://{AZURE_CUSTOM_DOMAIN}/static/'
STATIC_ROOT=os.path.join(BASE_DIR,"static")

MEDIA_URL = f'https://{AZURE_CUSTOM_DOMAIN}/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,"media")
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'student_app',
    'storages',
]

MIDDLEWARE = [
 
     #'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'student_app.LoginCheckMiddleWare.LoginCheckMiddleWare'
]

ROOT_URLCONF = 'student_system.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['student_app/templates'],
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

WSGI_APPLICATION = 'student_system.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        #'ENGINE':'django.db.backends.mysql',
        #'NAME':'student_system',
        #'USER':'student_system',
        #'PASSWORD':'student_management_password',
        #'HOST':'localhost',
        #'PORT':'3306'
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



STATIC_URL = '/static/'
AUTH_USER_MODEL="student_app.CustomUser"
AUTHENTICATION_BACKENDS=['student_app.EmailBackEnd.EmailBackEnd']


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_FILE_PATH=os.path.join(BASE_DIR,"sent_mails")

EMAIL_HOST="smtp.gmail.com"
EMAIl_PORT=587
EMAIL_HOST_USER="mailsend564@gmail.com"
EMAIL_HOST_PASSWORD="tgrnwjrenjamecos"
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL="Student System <GMAIl_EMAIL>"


# STATICFILES_STORAGE='whitenoise.storage.CompressedManifestStaticFilesStorage'
# import dj_database_url
# prod_db=dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(prod_db)
