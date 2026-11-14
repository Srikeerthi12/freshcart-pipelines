
import pika, json, random, time
from datetime import datetime

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.exchange_declare(exchange="rapido-dispatch", exchange_type="topic")

cities = {
    "bangalore": ["koramangala", "indiranagar", "whitefield"],
    "chennai": ["tnagar", "adyar", "velachery"]
}
types = ["ride", "food"]

for i in range(60):
    city = random.choice(list(cities))
    zone = random.choice(cities[city])
    order_type = random.choice(types)

    if (i + 1) % 10 == 0:
        message = {"id": i + 1, "city": city, "type": order_type, "ts": str(datetime.now())}
        routing_key = f"{city}.{order_type}"
    else:
        message = {"id": i + 1, "city": city, "zone": zone, "type": order_type, "ts": str(datetime.now())}
        routing_key = f"{city}.{zone}.{order_type}"

    channel.basic_publish(
        exchange="rapido-dispatch",
        routing_key=routing_key,
        body=json.dumps(message)
    )
    print("Sent:", routing_key, message)
    time.sleep(2)

connection.close()
