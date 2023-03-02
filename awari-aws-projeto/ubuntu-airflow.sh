#!/bin/bash

sudo apt-get install -y software-properties-common
sudo apt-add-repository universe

sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget -qO- https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo tee /etc/apt/trusted.gpg.d/pgdg.asc &>/dev/null
sudo apt update

sudo apt install postgresql postgresql-client -y

sudo systemctl enable postgresql

sudo systemctl start postgresql

sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'Str0ngP@ssw0rd';"

sudo -u postgres psql -c "CREATE DATABASE awari_imdb;"


# AirFlow Install
sudo apt-get update
sudo apt-get install -y python-setuptools
sudo apt install -y python3-pip
sudo apt-get install -y libmysqlclient-dev
sudo apt-get install -y libssl-dev
sudo apt-get install -y libkrb5-dev

pip3 install apache-airflow[s3,aws,postgres]
pip3 install typing_extensions
pip3 install 'apache-airflow[amazon]' boto3 pandas pyarrow fastparquet

cd ~
mkdir airflow
mkdir airflow/downloads

sudo chmod -R 777 airflow/downloads

mv airflow.cfg airflow

mv dags airflow

export AIRFLOW_HOME="/home/ubuntu/airflow"

export PYTHONPATH=$PYTHONPATH:$AIRFLOW_HOME/dags

export PATH="/home/ubuntu/.local/bin/:$PATH"

airflow db init

airflow users create \
    --username airflow \
    --password airflow \
    --firstname Admin \
    --lastname TheGuy \
    --role Admin \
    --email airflow@awari.com.br

airflow connections add 'pg_awari' \
    --conn-json '{
        "conn_type": "postgres",
        "login": "postgres",
        "password": "Str0ngP@ssw0rd",
        "host": "localhost",
        "port": 5432,
        "schema": "awari_imdb"
    }'

airflow variables set AWS_ACCESS_KEY_ID SUA_CHAVE_AQUI
airflow variables set AWS_REGION sa-east-1
airflow variables set AWS_SECRET_ACCESS_KEY SUA_SECRET_AQUI
airflow variables set AWS_BUCKET awari-de-nome-do-aluno

airflow webserver -D

airflow scheduler -D
