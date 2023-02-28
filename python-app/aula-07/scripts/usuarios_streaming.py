import pandas as pd

from time import sleep
from json import dumps
from kafka import KafkaProducer
from faker import Faker
from datetime import datetime
import random

fake = Faker("pt_BR")

producer = KafkaProducer(bootstrap_servers=['awari-kafka:9093'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))


for e in range(300):

    for _ in range(random.randint(1,7)):
        current_time = datetime.now()
        data = {
            'id': fake.unique.random_int(min=1, max=99999999),
            'nome' : fake.name(), 
            'email': fake.email(), 
            'endereco': fake.street_address().replace(",", "") + " " + fake.current_country(), 
            'criado_em': current_time.strftime("%Y-%m-%d %H:%M:%S")
        }

        # Descomentar linha abaixo para ver os dados sendo gerados    
        # print(data)

        producer.send('aula07-usuarios', value=data)

    sleep(random.randint(1,1))