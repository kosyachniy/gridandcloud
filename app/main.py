import json
from time import sleep
import pika
from pika.exceptions import AMQPConnectionError
from . import worker_selfie
import logging


def main():

    logging.basicConfig(filename="logs/sample.log", level=logging.INFO)

    consumer_cfg = json.load(open('cfg/rabbitmq_consumer_config.json', 'r'))
    handler_configs = json.load(open('cfg/handler_configs.json', 'r'))
    credentials_cfg = json.load(open('cfg/credentials.json', 'r'))

    credentials = pika.PlainCredentials(**credentials_cfg)
    connection = pika.BlockingConnection(pika.ConnectionParameters(credentials=credentials, **consumer_cfg))
    channel = connection.channel()

    logging.info("Connection established, channel created")

    channel.queue_declare(queue='check_user/selfie', durable=True)

    channel.basic_consume(
        on_message_callback=worker_selfie.construct_handler(**handler_configs['selfie']),
        queue='check_user/selfie')

    logging.info("Consuming methods declared, consuming started")

    channel.start_consuming()


if __name__ == '__main__':
    i_loop = True
    while i_loop:
        try:
            main()
        except pika.exceptions.AMQPConnectionError:
            logging.info("Waiting for AMPQ connect")
            sleep(1)
        except BaseException as e:
            logging.error(e)
            i_loop = False

