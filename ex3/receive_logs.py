import pika, sys, os

def main():
    # estabelece um canal de comunicação com o rabbitmq
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    
    channel.exchange_declare(exchange='logs', exchange_type='fanout')
    
    # cria uma fila que o próprio rabbitmq define o nome
    # com result.method.queue podemos verificar o nome dessa fila criada
    # a flag exclusive faz com que quando a conexão seja encerrada a queue seja deletada
    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue
    
    # cria a conexão entre a exchange e a queue que criamos, fazendo um 'binding' entre elas
    channel.queue_bind(exchange='logs',
                       queue=queue_name)
    
    print(' [*] Waiting for messages. To exit press CTRL+C')

    # o retorno da delivery_tag informa pro acknowledge se a mensagem foi recebida,
    # caso não tenha sido ele não irá perder a mensagem
    def callback(ch, method, properties, body):
        print(f" [x] {body}")

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    
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