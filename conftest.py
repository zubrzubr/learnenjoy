import os

import configurations


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learntoenjoy.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'TestingSite')


configurations.setup()
