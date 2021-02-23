from .base import * # pylint: disable=unused-wildcard-import


DEBUG = False
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', SECRET_KEY)

# Set ALLOWED_HOSTS to environment variable
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '127.0.0.1 .revibe.tech revibe.tech').split(' ')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('RDS_DB_NAME'),
        'USER': os.environ.get('RDS_USERNAME'),
        'PASSWORD': os.environ.get('RDS_PASSWORD'),
        'HOST': os.environ.get('RDS_HOSTNAME'),
        'PORT': os.environ.get('RDS_PORT'),
    },
}

# -----------------------------------------------------------------------------
##### AWS Configuration #####
# -----------------------------------------------------------------------------

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID', "base_key")
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', 'secret_key')

AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = 'us-east-2' # we still use Ohio for all of our static storage
AWS_DEFAULT_ACL = None
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
AWS_QUERYSTRING_AUTH = False


# -----------------------------------------------------------------------------
##### Static files (CSS, JavaScript, Images) #####
# https://docs.djangoproject.com/en/3.0/howto/static-files/
# -----------------------------------------------------------------------------

# https://docs.djangoproject.com/en/3.0/ref/settings/#static-url
STATIC_LOCATION = 'static'
STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/{APPLICATION_NAME}/"

# https://docs.djangoproject.com/en/3.0/ref/settings/#staticfiles-storage
# Only uncomment if you need static files for your application
# STATICFILES_STORAGE = 'project.storage_backends.StaticStorage'


# -----------------------------------------------------------------------------
##### Media Files #####
# -----------------------------------------------------------------------------

# https://docs.djangoproject.com/en/3.0/ref/settings/#media-url
MEDIA_LOCATION = 'media'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIA_LOCATION}/'

# https://docs.djangoproject.com/en/3.0/ref/settings/#default-file-storage
# Only uncomment if you need media files in your application
# DEFAULT_FILE_STORAGE = 'project.storage_backends.MediaStorage'


# OAuth Toolkit
OAUTH2_PROVIDER['RESOURCE_SERVER_INTROSPECTION_URL'] = os.environ.get("DJANGO_OAUTH2_PROVIDER_RESOURCE_SERVER_INTROSPECTION_URL", "https://api.revibe.tech/api/auth/o/introspect")
