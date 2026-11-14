
import pika, json, sys

name, pattern = sys.argv[1], sys.argv[2]

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.exchange_declare(exchange="rapido-dispatch", exchange_type="topic")

result = channel.queue_declare(queue="", exclusive=True)
queue = result.method.queue
channel.queue_bind(exchange="rapido-dispatch", queue=queue, routing_key=pattern)

print(f"{name} listening for {pattern}")

def callback(ch, method, properties, body):
    message = json.loads(body)
    if "zone" not in message:
        print("REJECTED:", message)
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)
    else:
        print(f"{name} received {method.routing_key}: {message}")
        ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=False)
channel.start_consuming()
