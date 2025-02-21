import sys
import pika

# estabelece um canal de comunicação com o rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# cria uma exchange que recebe do produtor e envia para uma fila (a fila posteriormente envia para o consumidor)
# o tipo 'fanout' indica que a exchange irá enviar as mensagens para todas as filas que conhece
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

# se a mensagem (enviada na hora de executar o .py) foi uma string vazia, será preenchida com Hello World
message = ' '.join(sys.argv[1:]) or "info: Hello World"

# o delivery_mode persistente faz com que a mensagem não se perca caso não consiga fazer o envio ou haja algum problema
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print(f" [X] Sent {message}")
connection.close()

