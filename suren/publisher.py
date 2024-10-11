import logging
from config import get_connection, configure_logging

log = logging.getLogger(__name__)


def main():
    configure_logging()
    with get_connection() as connection:
        log.info('Соединение установлено: %s', connection)
        with connection.channel() as channel:
            log.info('Канал установлен: %s', channel)
    while True:
        pass


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        log.info('Выполнение прервано пользователем')
    finally:
        log.info('Завершение работы')
