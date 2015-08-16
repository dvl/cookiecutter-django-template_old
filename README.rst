============================
Cookiecutter Django Template
============================

Esse projeto visa a prover uma estrutura inicial para seus projetos
com Django já incluindo diversas extensões que são comumente usadas
em diversos projetos.

********
Conteudo
********

* Django 1.8
* ``django-debug-toolbar`` e ``django-extensions`` porque todo projeto
  deveria usar isso.
* ``django-flat-theme`` pois possivelmente será padrão em uma futura versão
  do Django, então se acostume.
* ``settings.py`` compativel com 12factor_ usando ``python-decouple`` e
  ``dj-database-url``
* Home page customizada
* Página de login e troca de senha customizadas baseada no ``contrib.auth``
  (então talves as pessoas parem de reinventar a roda.).
* ``bower`` e ``django-compressor`` para lidar com arquivos estaticos.
* ``django-crispy-forms`` e ``django-floopyforms`` pois lidar com form no
  Django por padrão é horrivel.
* ``Procfile``, ``whitenoise``, ``waitress-server`` para deploy facil no
  Heroku.
* ``Dockerfile`` e ``docker-compose.yml`` para facilitar o desenvolvimento
  local com ``Docker``
* ``Makefile`` para facilitar com testes e ``coverage`` para relatórios de
  cobertura.
* ``bcrypt`` no lugar do ``pbkdf2``.

*************************
Iniciando um novo projeto
*************************

Primeiramente tenha instalado o `cookiecutter`, recomendo a instalação global
desse pacote

.. code:: shell

    $ sudo pip install cookiecutter

Com o cookiecutter instalado baixe o template inicial:

.. code:: shell

   $ cookiecutter https://github.com/dvl/django-cookiecutter-template

Algumas perguntas serão feitas, responda de acordo com sua necessidades.

************
Dependencias
************

Esse projeto faz uso das mais atuais tendencias para facilitar o
desenvolvimento front-end do projeto, como ``bower``, ``sass``, ``gulp``, etc...
portanto será necessária a instalação do ``node.js`` com ``npm`` e ``Ruby`` com
``gem`` e ``bundle``.

Caso você já tenha essas depedencias instaladas basta digitar:

.. code:: shell

    $ npm install

    $ bundle install

****************
requirements.txt
****************

Para garantirmos que sempre vamos ter a ultima versão das dependencias usadas
no nosso requirements usamos o ``pip-tools`` nesse projeto para instala-lo faça

.. code:: shell

    $ pip install pip-tools

Nosso arquivo ``requirements.txt`` será gerado com base no ``requirements.in``
para isso basta digitar

.. code:: shell

     $ pip-compile

Agora você pode instalar normalmente como você já está acostumado ou...

.. code:: shell

    $ pip-sync

Para garantir que somente as dependencias listadas no requirements fiquem
instaladas.

Leia mais sobre o pip-tools_.

********
12factor
********

Esse template foi construido com 12factor_ em mente, então edite o arquivo
que guarda suas variaveis de ambiente e é referenciado no `settings.py`

    $ vim .env

***
Run
***

Você pode iniciar o projeto com:

.. code:: shell

    $ python manage.py runserver


.. _pip-tools: https://koed00.github.io/managed-environments-with-piptools/
.. _12factor: http://12factor.net/
