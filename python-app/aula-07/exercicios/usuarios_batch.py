import os
import glob
import pandas as pd

import boto3
from io import StringIO

# Caminho dentro da imagem python-app para os arquivos a serem processados
path = '/home/awari/app/aula-07/ingest/batch/'

# Carrega todos os CSV da pasta
csv_files = glob.glob(os.path.join(path, "*.csv"))

# Cria um cliente com o MinIO
client = boto3.client('s3', 
    endpoint_url='http://awari-minio-nginx:9000',
    aws_access_key_id='mnYOiUf07UBjjJwf',
    aws_secret_access_key='1Qu7X3EmbIYDNXUiuvFSDUJwJ4fWdyT5',
    aws_session_token=None,
    config=boto3.session.Config(signature_version='s3v4'),
    verify=False,
    region_name='sa-east-1'
)

# Percorre cada CSV encontrado na pasta
for f in csv_files:
      
    # Inicia a leitura do CSV
    df = pd.read_csv(f)
      
    # Print com a localização, nome do arquivo, conteudo e o DataFrame
    print('Localização:', f)
    print('Nome do arquivo:', f.split("/")[-1])
    print('Conteudo:')
    print(df)

    # Carrega em Buffer o conteudo do arquivo CSV
    csv_buffer = StringIO()
    csv = df.to_csv(csv_buffer, index=False)
    # Salva no S3/MinIO
    client.put_object(Body=csv_buffer.getvalue(), Bucket='aula-07', Key="usuarios/batch/" + f.split("/")[-1])

    # Remove o csv da pasta
    os.remove(f)