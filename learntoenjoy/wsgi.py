"""
WSGI config for learntoenjoy project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learntoenjoy.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'ProdSettings')

from configurations.wsgi import get_wsgi_application

application = get_wsgi_application()
