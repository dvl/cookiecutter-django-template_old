FROM python:2

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y \
                python-dev \
                libfreetype6-dev \
                libjpeg-dev \
                zlib1g-dev \
                mysql-client \
                libmysqlclient-dev \
                postgresql-client \
                libpq-dev \
                libffi-dev \
                libssl-dev \
                gcc \
        --no-install-recommends && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

# package.json

# Gemfile

COPY . /usr/src/app
