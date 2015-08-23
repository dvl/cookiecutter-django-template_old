FROM nodesource/jessie:0.12.7

MAINTAINER André Luiz <contato@xdvl.info>

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y \
                build-essential \
                gcc \
                libffi-dev \
                libfreetype6-dev libjpeg-dev \
                libssl-dev \
                mysql-client libmysqlclient-dev \
                postgresql-client libpq-dev \
                python-dev python-pip \
                zlib1g-dev \
        --no-install-recommends && rm -rf /var/lib/apt/lists/*

RUN pip install -U pip

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

# COPY package.json bower.json /usr/src/app/
# RUN npm install

ENV PATH node_modules/.bin/:$PATH

COPY . /usr/src/app

RUN useradd -u 1000 -m -s /bin/bash app
RUN chown -R app:app .

USER app
