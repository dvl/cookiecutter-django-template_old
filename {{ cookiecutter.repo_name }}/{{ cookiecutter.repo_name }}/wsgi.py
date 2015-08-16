# -*- coding: utf-8 -*-

"""
WSGI config for {{ cookiecutter.project_name }} project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ cookiecutter.repo_name }}.settings")

from django.core.wsgi import get_wsgi_application
{% if cookiecutter.use_whitenoise == 'y' or cookiecutter.use_heroku == 'y' %}from whitenoise.django import DjangoWhiteNoise{% endif %}

application = get_wsgi_application()
{% if cookiecutter.use_whitenoise == 'y' or cookiecutter.use_heroku == 'y' %}application = DjangoWhiteNoise(application){% endif %}
