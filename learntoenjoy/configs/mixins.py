from configurations import values


class DevMixin(object):
    DEBUG = values.BooleanValue(True)


class TestingMixin(object):
    TESTING = True
    LOGGING = {}
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }


class ProdMixin(object):
    EMAIL_HOST = values.Value(default='localhost')


class CeleryProdMixin(object):
    pass
