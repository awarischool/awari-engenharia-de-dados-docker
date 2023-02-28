import pandas as pd

from time import sleep
from faker import Faker
from datetime import datetime
import random

fake = Faker("pt_BR")


for e in range(10):

    lista_de_usuarios = []
    cont = 0;

    current_time = datetime.now()

    for _ in range(random.randint(100,2000)):
        cont = cont + 1;
        data = {
            'id': fake.unique.random_int(min=1, max=99999999),
            'nome' : fake.name(), 
            'email': fake.email(), 
            'endereco': fake.street_address().replace(",", "") + " " + fake.current_country(), 
            'criado_em': current_time.strftime("%Y-%m-%d %H:%M:%S")
        }
        lista_de_usuarios.append(data)

    df = pd.DataFrame.from_dict(lista_de_usuarios)

    # Descomentar linha abaixo para ver os dados sendo gerados
    # print(df, current_time)

    novo_arquivo = current_time.strftime("%Y-%m-%d-%H%M%S") + '.csv'
    df.to_csv("/home/awari/app/aula-07/ingest/batch/" + novo_arquivo, header=True, index=False)
    
    sleep(random.randint(1,2))