import pika, sys, os, time

def main():
    # estabelece um canal de comunicação com o rabbitmq
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()


    # declara novamente a fila, caso ela não tenha sido criada antes (o send.py pode rodar depois), ele cria, 
    # se esta fila já existir, ele não cria outra
    channel.queue_declare(queue='hello')

    # função que será 'inscrita' na fila, para funcionar toda vez que for recebido uma mensagem
    def callback(ch, method, properties, body):
        print(f" [X] Received {body.decode()}")
        time.sleep(body.count(b'.'))
        print(f" [X] Done")
    
    # passamos para o consumidor que ele deve consumir da fila 'hello' e executar a função callback quando fize
    # de forma resumida, o ack funciona como um retorno do nosso consumo para a fila, informando se recebemos a mensagem ou houve alguma erro
    channel.basic_consume(queue='hello',
                          auto_ack=True,
                          on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
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