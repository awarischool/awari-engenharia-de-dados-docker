import os
import glob
import pandas as pd
import boto3
import botocore
import json

from kafka import KafkaConsumer
from json import loads
from datetime import datetime
from io import StringIO

# Metodo para salvar no S3/MinIO
def save_key_to_s3(data_frame, key):
    csv_buffer = StringIO()
    csv = data_frame.to_csv(csv_buffer, index=False)
    client.put_object(Body=csv_buffer.getvalue(), Bucket='aula-07', Key=key)
    response = client.get_object(Bucket='aula-07', Key=key)
    return response

# Caminho para o CSV que possui os usuários sendo carregados constantemente
path = '/home/awari/app/aula-07/ingest/streaming/usuarios.csv'

# Pegamos data e hora atuais
current_time = datetime.now()

# Cria cliente com o S3/Minio
client = boto3.client('s3', 
    endpoint_url='http://awari-minio-nginx:9000',
    aws_access_key_id='mnYOiUf07UBjjJwf',
    aws_secret_access_key='1Qu7X3EmbIYDNXUiuvFSDUJwJ4fWdyT5',
    aws_session_token=None,
    config=boto3.session.Config(signature_version='s3v4'),
    verify=False,
    region_name='sa-east-1'
)

# Caminhos o S3/MinIO para um arquivo chamado usuarios.csv
key_usuarios = "usuarios/streaming/usuarios.csv"

# O try Catch abaixo checa se ja existe um usuarios.csv no bucket
# casão não exista, é feito o upload de um CSV em Branco para que possamos iniciar
try:
    response = client.get_object(Bucket='aula-07', Key=key_usuarios)
    status = response.get("ResponseMetadata", {}).get("HTTPStatusCode")
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "NoSuchKey":
        # Se Key não existir.
        status_df = pd.read_csv("/home/awari/app/aula-07/scripts/diferencial_usuarios_em_branco.csv")
        response = save_key_to_s3(status_df, key_usuarios)

usuarios_df = pd.read_csv(response.get("Body"))
print(usuarios_df)
# Fim da validação do arquivo de usuários

# Cria um consumidor com o Kafka
consumer = KafkaConsumer(
    'aula07-usuarios',
     bootstrap_servers=['awari-kafka:9093'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='pipeline-python',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

# Começa a percorrer as mensagens encontradas no kafka
for message in consumer:
    message = message.value
    
    # Converte a mensage que esta em JSON para DataFrame
    usuarios_df = usuarios_df.append(message, ignore_index=True)
    # Salva como CSV no bucket
    response = save_key_to_s3(usuarios_df, key_usuarios)
    print(usuarios_df)

