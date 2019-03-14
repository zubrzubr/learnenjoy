from learntoenjoy.configs.common import BaseSettings
from learntoenjoy.configs.mixins import DevMixin, ProdMixin, TestingMixin


class DevSettings(DevMixin, BaseSettings):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'postgres',
            'HOST': 'localhost',
            'PORT': 5432
        }
    }


class ProdSettings(ProdMixin, BaseSettings):
    pass


class TestSettings(TestingMixin, DevMixin, BaseSettings):
    pass
