import logging
from config import get_connection, configure_logging

log = logging.getLogger(__name__)


def produce_message(channel):
    message_body = 'Hello world!'
    log.debug('Отправка сообщения... !', message_body)
    channel.basic_publish(
        exchange='',
        routing_key='hello',
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
