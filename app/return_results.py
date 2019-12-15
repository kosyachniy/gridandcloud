import json
from functools import lru_cache
import pika
import logging


@lru_cache(1)
def _get_sender_channel():
    sender_cfg = json.load(open('cfg/rabbitmq_sender_config.json', 'r'))
    credentials_cfg = json.load(open('cfg/credentials.json', 'r'))

    credentials = pika.PlainCredentials(**credentials_cfg)
    connection = pika.BlockingConnection(pika.ConnectionParameters(credentials=credentials, **sender_cfg))
    channel = connection.channel()
    channel.queue_declare(queue='computation_results', durable=True)

    logging.info("Bad adder channel declared")

    return channel


def return_results(id: str, correct: bool) -> None:

    logging.info(f"In returning results, id: {id}")

    _get_sender_channel().basic_publish(
        exchange='',
        routing_key='results',
        body=json.dumps(
            {
                'id': id,
                'res': correct
            }
        ),
        properties=pika.BasicProperties(
            delivery_mode=2
        ))
