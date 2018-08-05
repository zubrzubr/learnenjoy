from learntoenjoy.configs.common import BaseSettings
from learntoenjoy.configs.mixins import DevMixin, ProdMixin, TestingMixin


class DevSettings(DevMixin, BaseSettings):
    pass


class ProdSettings(ProdMixin, BaseSettings):
    pass


class TestSettings(TestingMixin, DevMixin, BaseSettings):
    pass
