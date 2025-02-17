import pika 

# estabelece um canal de comunicação com o rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters('172.17.0.2'))
channel = connection.channel()

# declara uma fila nomeada de hello
channel.queue_declare(queue='hello')

# faz uma publicação básica no canal de comunicação, com routing_key sendo como uma espécie de 'identificador' pra essa rota
channel.basic_publish(exchange='', 
                        routning_key='hello',
                        body='Hello World!')
print(" [X] Send 'Hello World! '")

connection.close()