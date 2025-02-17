# declara novamente a fila, caso ela não tenha sido criada antes (o send.py pode rodar depois), ele cria, 
# se esta fila já existir, ele não cria outra
channel.queue_declare(queue='hello')

# função que será 'inscrita' na fila, para funcionar toda vez que for recebido uma mensagem
def callback(ch, method, properties, body):
        print(f" [X] Received {body}")
    
# passamos para o consumidor que ele deve consumir da fila 'hello' e executar a função callback quando fize
# de forma resumida, o ack funciona como um retorno do nosso consumo para a fila, informando se recebemos a mensagem ou houve alguma erro
channel.basic_consume(queue='hello',
                        auto_ack=True,
                        on_message_callback=callback)

