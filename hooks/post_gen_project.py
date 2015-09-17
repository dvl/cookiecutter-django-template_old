# -*- coding: utf-8 -*-

import fileinput
import os
import shutil
import sys

for line in fileinput.input(".env-example", inplace=True):
    if line.startswith('SECRET_KEY='):
        print("SECRET_KEY={}".format(os.urandom(24).encode('hex')))
    else:
        print(line.replace('\n', ''))


repo_name = '{{ cookiecutter.repo_name }}'

use_postgres = '{{ cookiecutter.use_postgres }}' == 'y'
use_mysql = '{{ cookiecutter.use_mysql }}' == 'y'
use_compressor = '{{ cookiecutter.use_compressor }}' == 'y'
use_memcached = '{{ cookiecutter.use_memcached }}' == 'y'
use_elasticsearch = '{{ cookiecutter.use_elasticsearch }}' == 'y'
use_celery = '{{ cookiecutter.use_celery }}' == 'y'
use_celery_with_rabbitmq = '{{ cookiecutter.use_celery_with_rabbitmq }}' == 'y'
use_celery_with_redis = '{{ cookiecutter.use_celery_with_redis }}' == 'y'
use_celery_beat = '{{ cookiecutter.use_celery_beat }}' == 'y'
use_whitenoise = '{{ cookiecutter.use_whitenoise }}' == 'y'
use_docker = '{{ cookiecutter.use_docker }}' == 'y'
use_heroku = '{{ cookiecutter.use_heroku }}' == 'y'
use_bcrypt = '{{ cookiecutter.use_bcrypt }}' == 'y'
use_newrelic = '{{ cookiecutter.use_newrelic }}' == 'y'

if not use_heroku:
    os.remove('.buildpacks')
    os.remove('Procfile')

if not use_docker:
    os.remove('Dockerfile')
    os.remove('docker-compose.yml')

if not use_newrelic:
    os.remove('newrelic.ini')

if not use_celery:
    os.remove(os.path.join(repo_name, 'celery.py'))

if not use_elasticsearch:
    shutil.rmtree(os.path.join(repo_name, 'templates', 'search'))

shutil.copyfile('.env-example', '.env')

if sys.platform in ['linux', 'linux2', 'darwin']:
    os.chmod('manage.py', 0744)
