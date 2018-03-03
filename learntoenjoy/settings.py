from os.path import join, dirname, abspath, pardir

from learntoenjoy.configs.common import BaseSettings
from learntoenjoy.configs.mixins import DevMixin, ProdMixin, TestingMixin


class DevDefaultSite(DevMixin, BaseSettings):
    pass

class ProdDefaultSite(ProdMixin, BaseSettings):
    pass

class TestingSite(TestingMixin, DevMixin, BaseSettings):
    pass
