import logging

from config import (MQ_EXCHANGE, MQ_ROUTING_KEY, configure_logging,
                    get_connection)

log = logging.getLogger(__name__)


def produce_message(channel):

    queue = channel.queue_declare(queue=MQ_ROUTING_KEY)
    log.info(f'Очередь создана... {MQ_ROUTING_KEY} {queue}')
    message_body = 'Hello world'
    log.info('Отправка сообщения... !', message_body)
    channel.basic_publish(
        exchange=MQ_EXCHANGE,
        routing_key=MQ_ROUTING_KEY,
        body='Hello world!'
    )
    log.warning('Сообщение опубликовано!', message_body)


def main():
    configure_logging()
    with get_connection() as connection:
        log.info('Соединение установлено: %s', connection)
        with connection.channel() as channel:
            log.info('Канал установлен: %s', channel)
            produce_message(channel=channel)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        log.info('Выполнение прервано пользователем')
    finally:
        log.info('Завершение работы')
