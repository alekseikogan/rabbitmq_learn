import logging

import pika

RMQ_HOST = 'localhost'
RMQ_PORT = 5672
RMQ_USER = 'guest'
RMQ_PASSWORD = 'guest'

MQ_EXCHANGE = ''
MQ_ROUTING_KEY = 'news'

connection_params = pika.ConnectionParameters(
    host=RMQ_HOST,
    port=RMQ_PORT,
    credentials=pika.PlainCredentials(RMQ_USER, RMQ_PASSWORD)
)


def get_connection() -> pika.BlockingConnection:
    return pika.BlockingConnection(
        parameters=connection_params
    )


def configure_logging(level=logging.INFO):
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(funcName)s - %(module)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
