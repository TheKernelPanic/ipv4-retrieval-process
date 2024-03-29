import json
from configuration import parameters
from messages.rabbitmq import RabbitMQHandler
from repository.model import IpV4
from repository.session import session

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
    ip_v4 = IpV4(
        ip=payload['ip_v4'],
        provider=payload['provider']
    )
    session.add(ip_v4)
    session.commit()


rabbitmq_handler.consume(
    on_message_callable=on_message_callable
)
