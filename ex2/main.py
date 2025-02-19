import pika, sys, os, time

def main():
    # estabelece um canal de comunicação com o rabbitmq
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # cria uma fila com durabilidade pra meso que haja um crash ou seja reiniciado o Rabbitmq
    # ele continue mantendo a fila e suas informações
    channel.queue_declare(queue='task_queue', durable=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')

    # o retorno da delivery_tag informa pro acknowledge se a mensagem foi recebida,
    # caso não tenha sido ele não irá perder a mensagem
    def callback(ch, method, properties, body):
        print(f" [x] Received {body.decode()}")
        time.sleep(body.count(b'.'))
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='task_queue', on_message_callback=callback)
    
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)