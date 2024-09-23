Código 9: Monitoramento em Tempo Real com Apache Kafka
from kafka import KafkaProducer
import json
import time

# Configura o produtor Kafka
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Simula o envio de dados em tempo real para o Kafka
for i in range(100):
    data = {
        'user_id': i,
        'event_type': 'click',
        'item_id': f'item_{i}',
        'timestamp': time.time()
    }
    producer.send('user_events', value=data)
    time.sleep(1)

producer.flush()
