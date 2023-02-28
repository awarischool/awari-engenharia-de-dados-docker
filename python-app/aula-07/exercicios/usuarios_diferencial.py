import os
import glob
import pandas as pd
import boto3
import botocore

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
path = '/home/awari/app/aula-07/ingest/diferencial/usuarios.csv'

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

# Caminhos o S3/MinIO para um arquivo chamado status.csv e usuarios.csv
# o Status CSV contem a data hora do ultimo usuário importado, por isso ele é importante
key_status = "usuarios/diferencial/status.csv"
key_usuarios = "usuarios/diferencial/usuarios.csv"

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

# O try/Catch abaixo checa se existe um status.csv no bucket
# casão não exista, é feito o upload de um CSV em Branco para que possamos iniciar
try:
    response = client.get_object(Bucket='aula-07', Key=key_status)
    status = response.get("ResponseMetadata", {}).get("HTTPStatusCode")
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "NoSuchKey":
        # Se Key não existir.
        data = {'ultima_atualizacao': current_time.strftime("%Y-%m-%d %H:%M:%S") }
        status_df = pd.read_csv("/home/awari/app/aula-07/scripts/diferencial_status.csv")
        response = save_key_to_s3(status_df, key_status)

status_df = pd.read_csv(response.get("Body"))
# É Carregado na memoria a data hora da ultima atualização, se arquivo não existir e foi upado agora
# a data hora e atual é igual a: 1999-01-01 00:00:01 para que possamos pegar os dados recentes
status_datetime_serie = pd.to_datetime(status_df['ultima_atualizacao'], format='%Y-%m-%d %H:%M:%S')
print(status_datetime_serie.iloc[0])
# Fim da validação de status

# Carregando o CSV de usuários localmente
df = pd.read_csv(path)

# Filtra os usuários com data em criado_em > que a data hora da ultima atualização
usuarios_filtrados_por_data = df[df['criado_em'] > str(status_datetime_serie.iloc[0])]
usuarios_df = usuarios_df.append(usuarios_filtrados_por_data)
print(usuarios_df)

# Pega a data do usuário mais recente
most_recent_date = usuarios_df['criado_em'].max()
status_df.iloc[0] = usuarios_df['criado_em'].max()
print(status_df)

# Atualiza o arquivo de usuários no bucket
response = save_key_to_s3(usuarios_df, key_usuarios)

# Atualiza o arquivo de status no bucket com data_hora do usuário mais recenete criado
response = save_key_to_s3(status_df, key_status)
   