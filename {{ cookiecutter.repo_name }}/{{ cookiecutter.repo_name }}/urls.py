# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home/index.html'), name='index'),
    {% if cookiecutter.use_elasticsearch == 'y' %}url(r'^search/', include('haystack.urls')),{% endif %}
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('django.contrib.auth.urls')),
]
