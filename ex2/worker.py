import time, pika

# estabelece um canal de comunicação com o rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# declara novamente a fila, caso ela não tenha sido criada antes (o send.py pode rodar depois), ele cria, 
# se esta fila já existir, ele não cria outra
channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

# função que será 'inscrita' na fila, para funcionar toda vez que for recebido uma mensagem
def callback(ch, method, properties, body):
        print(f" [X] Received {body.decode()}")
        time.sleep(body.count(b'.'))
        print(f" [X] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)

# a linha seguinte faz com que a mensagem seja distruibuida de forma a considerar as ocupações de consumidor
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)
    
# passamos para o consumidor que ele deve consumir da fila 'hello' e executar a função callback quando fize
# de forma resumida, o ack funciona como um retorno do nosso consumo para a fila, informando se recebemos a mensagem ou houve alguma erro
channel.basic_consume(queue='hello', on_message_callback=callback)

channel.start_consuming()
