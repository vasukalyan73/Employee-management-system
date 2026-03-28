"""
WSGI config for emp_details project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'emp_details.settings')

application = get_wsgi_application()
