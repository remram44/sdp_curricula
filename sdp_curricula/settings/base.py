# Django settings for sdp_curricula project.
import os
import sys

#PROJECT_ROOT = os.path.join(os.path.dirname(__file__), '..', '..')
PROJECT_ROOT = '/home/merbroussard/axis2/stacked-up'
# Modify sys.path to include the lib directory
sys.path.append(os.path.join(PROJECT_ROOT, "lib"))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = "70ca2857c8bd8c80401ff4e65d2ebf48"

ADMINS = (
    ('Paul', 'starsinmypockets@gmail.com'),
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#         'LOCATION': '/var/tmp/django_cache',
#         'TIMEOUT': 0,
#         'OPTIONS': {
#             'MAX_ENTRIES': 1000
#         }
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'stacked',
        'USER': 'stacked',
        'PASSWORD': '@x1s2013',
        'HOST': '',  # Set to empty string for localhost.
        'PORT': '',  # Set to empty string for default.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '/home/merbroussard/webapps/static/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = 'http://merbroussard.webfactional.com/static/media/'

# CKEDITOR 
CKEDITOR_UPLOAD_PATH = '/home/merbroussard/webapps/static/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
#STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_ROOT = '/home/merbroussard/webapps/static/'
# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = 'http://merbroussard.webfactional.com/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'staticfiles', '/home/merbroussard/webapps/static/ckeditor/'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
        'django.template.loaders.app_directories.Loader',
)
#     'django.template.loaders.eggs.Loader',

MIDDLEWARE_CLASSES = (
    # 'django.middleware.cache.UpdateCacheMiddleware',
    # 'django.middleware.common.CommonMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'aloha_editor.middleware.AlohaEditorMiddleware',
)

ROOT_URLCONF = 'sdp_curricula.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'sdp_curricula.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth'
)

INSTALLED_APPS = (
    'adminsortable',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'ckeditor',
    'south',
    'debug_toolbar',
#    'devserver',
    'compressor',
    'debug_toolbar',
    'tastypie',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
#    Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'articles',
    'schools',
    'students',
    'curricula',
    'vendors',
    'core'
)

EMAIL_SUBJECT_PREFIX = '[sdp_curricula] '

INTERNAL_IPS = ('127.0.0.1', '10.0.2.2')

# django-debug-toolbar settings
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
       'logfile': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': "/home/merbroussard/django.log",
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'console':{
            'level':'INFO',
            'class':'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django' : {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
        }
    },
    'formatters' : {
        'standard': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
    }
}

ALLOWED_HOSTS = '*'

if 'DATABASE_URL' in os.environ:
    import dj_database_url
    DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}
