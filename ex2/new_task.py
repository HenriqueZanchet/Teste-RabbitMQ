import sys, pika

# estabelece um canal de comunicação com o rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# se a mensagem (enviada na hora de executar o .py) foi uma string vazia, será preenchida com Hello World
message = ' '.join(sys.argv[1:]) or "Hello World"

channel.basic_publish(exchange='', 
                        routing_key='hello',
                        body=message)
print(f" [X] Sent {message}")

