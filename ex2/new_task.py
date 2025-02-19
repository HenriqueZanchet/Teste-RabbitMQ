import sys, pika

# estabelece um canal de comunicação com o rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

# se a mensagem (enviada na hora de executar o .py) foi uma string vazia, será preenchida com Hello World
message = ' '.join(sys.argv[1:]) or "Hello World"

# o delivery_mode persistente faz com que a mensagem não se perca caso não consiga fazer o envio ou haja algum problema
channel.basic_publish(exchange='', 
                      routing_key='task_queue',
                      body=message,
                      # salva as mensagens para que elas não sejam perdidas
                      properties=pika.BasicProperties(
                          delivery_mode = pika.DeliveryMode.Persistent
                      ))
print(f" [X] Sent {message}")
connection.close()

