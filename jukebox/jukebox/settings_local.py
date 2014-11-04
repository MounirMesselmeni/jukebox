DEBUG = True
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = "dfsdfsfd3334FDDSFSDFSD"

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
)

SOCIAL_AUTH_ENABLED_BACKENDS = (['social_auth.backends.facebook.FacebookBackend'])