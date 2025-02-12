import pika

connection_parameters = pika.ConnectionParameters('localhost:15672')

coneection = pika.BlockingConnection(connection_parameters)

channel = connection.chanel()

channel.queue_declare(queue='letterbox')

message = "esta é a minha primeira mensagem"

channel.basic_publish(exchange='', routing_key='letterbox', body=message)

print(f"enviando mensagem: {message}")

connection.close()