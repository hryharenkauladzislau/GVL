from kafka import KafkaConsumer
import json
from collections import Counter

consumer = KafkaConsumer(
    'user_actions',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='user_group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

action_counter = Counter()

print("Слушаем сообщения...")
for message in consumer:
    data = message.value
    if data['action'] == 'purchase':
        print("Покупка:", data)
    action_counter[data['action']] += 1
    print("Статистика:", dict(action_counter))
