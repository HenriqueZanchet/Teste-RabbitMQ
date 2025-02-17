import pika 

connection = pika.BlockingConnection(pika.ConnectionParameters('172.17.0.2'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', 
                        routning_key='hello',
                        body='Hello World!')
print(" [X] Send 'Hello World! '")

connection.close()