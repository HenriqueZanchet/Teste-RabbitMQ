import pika 

# estabelece um canal de comunicação com o rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# declara uma fila nomeada de hello
channel.queue_declare(queue='hello')

# faz uma publicação básica no canal de comunicação, com routing_key sendo como uma espécie de 'identificador' pra essa rota
channel.basic_publish(exchange='', 
                      routing_key='hello',
                      body='Hello World!')
print(" [X] Send 'Hello World! '")

connection.close()