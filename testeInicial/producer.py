import pika
import time 
import random

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='letterbox')

messageId = 1

while(True):
    message = "Hello this is my first mesage"

    channel.basic_publish(exchange='', routing_key='letterbox', body=message)

    time.sleep(random.randint(1, 4))

    print(f"Mensagem enviada: {message}")

    messageId+=1