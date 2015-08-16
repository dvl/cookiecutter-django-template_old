============================
Cookiecutter Django Template
============================

Esse projeto visa a prover uma estrutura inicial para seus projetos
com Django já incluindo diversas extensões que são comumente usadas
em diversos projetos.

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
desenvolvimento front-end do projeto, como `bower`, `sass`, `gulp`, etc...
portanto será necessária a instalação do `node.js` com `npm` e `Ruby` com
`gem` e `bundle`.

Caso você já tenha essas depedencias instaladas basta digitar:

.. code:: shell

    $ npm install

    $ bundle install

Ou use a versão com Docker e resolvemos tudo isso pra você ;)

****************
requirements.txt
****************

Para garantirmos que sempre vamos ter a ultima versão das dependencias usadas
no nosso requirements usamos o `pip-tools` nesse projeto para instala-lo faça

.. code:: shell

    $ pip install pip-tools

Nosso arquivo `requirements.txt` será gerado com base no `requirements.in`
para isso basta digitar

.. code:: shell

     $ pip-compile

Agora você pode instalar normalmente como você já está acostumado ou...

... code:: shell

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



    $ python manage.py runserver


.. _pip-tools: https://koed00.github.io/managed-environments-with-piptools/
.. _12factor: http://12factor.net/
