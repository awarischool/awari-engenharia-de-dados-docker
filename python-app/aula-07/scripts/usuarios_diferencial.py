import pandas as pd

from time import sleep
from faker import Faker
from datetime import datetime
import random
import csv

fake = Faker("pt_BR")

for e in range(300):

    lista_de_usuarios = []

    current_time = datetime.now()
    for _ in range(random.randint(1,53)):
        address = fake.street_address() + " " + fake.current_country()
        data = {
            'id': fake.unique.random_int(min=1, max=99999999),
            'nome' : fake.name(), 
            'email': fake.email(), 
            'endereco': address.replace(",", ""), 
            'criado_em': current_time.strftime("%Y-%m-%d %H:%M:%S")
        }
        lista_de_usuarios.append(data)

    df = pd.DataFrame.from_dict(lista_de_usuarios)

    # Descomentar linha abaixo para ver os dados sendo gerados
    # print(df, current_time)
    novo_arquivo = 'usuarios.csv'
    df.to_csv("/home/awari/app/aula-07/ingest/diferencial/" + novo_arquivo, header=False, mode='a', index=False, lineterminator='\n')
    
    sleep(random.randint(1,2))