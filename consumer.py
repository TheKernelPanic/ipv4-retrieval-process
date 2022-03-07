import json
from configuration import parameters
from messages.rabbitmq import RabbitMQHandler

rabbitmq_handler = RabbitMQHandler(
    host=parameters['rabbitmq']['host'],
    username=parameters['rabbitmq']['username'],
    password=parameters['rabbitmq']['password']
)


def on_message_callable(channel, method_frame, header_frame, body) -> None:
    """
    TODO: Persist
    :param channel:
    :param method_frame:
    :param header_frame:
    :param body:
    :return:
    """
    payload = json.loads(body)
    print(payload)


rabbitmq_handler.consume(
    on_message_callable=on_message_callable
)
