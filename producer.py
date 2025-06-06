from kafka import KafkaProducer
import json
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    user_id = int(input("Введите ID пользователя: "))
    action = input("Введите действие (например, purchase): ")
    timestamp = datetime.now().isoformat()

    message = {
        "user_id": user_id,
        "action": action,
        "timestamp": timestamp
    }

    producer.send('user_actions', value=message)
    print("Отправлено:", message)
