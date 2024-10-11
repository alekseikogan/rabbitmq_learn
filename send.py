import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='localhost',
        port=5672)
)  # подключаемся к серверу localhost

channel = connection.channel()  # создаем канал

channel.queue_declare(queue='hello')  # создали очередь с именем hello

channel.basic_publish(
    exchange='',
    routing_key='hello',  # название очереди
    body='Hello World!',  # сообщение
    )

print(" [x] Sent 'Hello World!'")

connection.close()
