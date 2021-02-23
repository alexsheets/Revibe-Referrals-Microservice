from .base import * # pylint: disable=unused-wildcard-import


# -----------------------------------------------------------------------------
##### Media Files #####
# -----------------------------------------------------------------------------

# https://docs.djangoproject.com/en/3.0/ref/settings/#media-url
MEDIA_URL = '/media/'

# https://docs.djangoproject.com/en/3.0/ref/settings/#media-root
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')