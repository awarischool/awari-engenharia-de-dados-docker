from time import sleep
from json import dumps
from kafka import KafkaProducer

# Cria um producer, responsavel por enviar mensagens ao Kafka
producer = KafkaProducer(bootstrap_servers=['awari-kafka:9093'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))


# Envia mensagens a cada 5 segundos para o Kafka Aleatoriamente
for e in range(1000):
    data = {'number' : e}
    producer.send('numtest', value=data)
    sleep(5)