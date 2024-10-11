import logging
from config import get_connection, configure_logging

log = logging.getLogger(__name__)


def main():
    configure_logging()
    connection = get_connection()
    log.info('Соединение установлено: %s', connection)
    while True:
        pass


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        log.info('Выполнение прервано пользователем')
    finally:
        log.info('Завершение работы')
