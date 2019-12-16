import json
from functools import lru_cache
import pika
import pymongo
import logging


@lru_cache(1)
def _get_sender_channel():
    sender_cfg = json.load(open('cfg/rabbitmq_sender_config.json', 'r'))
    credentials_cfg = json.load(open('cfg/credentials.json', 'r'))

    credentials = pika.PlainCredentials(**credentials_cfg)
    connection = pika.BlockingConnection(pika.ConnectionParameters(credentials=credentials, **sender_cfg))
    channel = connection.channel()
    channel.queue_declare(queue='computation_results', durable=True)
    return channel


def return_results(id: str, correct: bool) -> None:

    print(f"In returning results, id: {id}")

    pymongo.MongoClient(
        'mongodb://{login}:{password}@ds018839.mlab.com:18839/user'.format(
            **json.load(open('./cfg/mongo_config.json'))
        )
    )['user'].update_one(
        {
            'image': id
        },
        {
            '$set': {
                'status': 2,
                'result': correct
            }
        },
        upsert=False
    )


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
