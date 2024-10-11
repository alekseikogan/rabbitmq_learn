import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='localhost',
        port=5672)
)  # подключаемся к серверу localhost

channel = connection.channel()  # создаем канал

channel.queue_declare(queue='hello')  # создали очередь с именем hello


def callback(ch, method, properties, body):
    print(f" [x] Получено {body}")


channel.basic_consume(
    queue='hello',
    on_message_callback=callback,
    auto_ack=True)


print(' [*] Ждем сообщения. To exit press CTRL+C')
channel.start_consuming()
