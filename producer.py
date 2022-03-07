import os
import sys
from retrieval.provider import AWSRanges
import ipaddress
from messages.rabbitmq import RabbitMQHandler
from configuration import parameters

if len(sys.argv) == 1:
    raise Exception('Missing argument')

supported_providers = {
    'aws': AWSRanges()
}

if not sys.argv[1].lower() in supported_providers:
    raise Exception('Unsupported provider')
else:
    provider = supported_providers[sys.argv[1].lower()]


rabbitmq_handler = RabbitMQHandler(
    host=parameters['rabbitmq']['host'],
    username=parameters['rabbitmq']['username'],
    password=parameters['rabbitmq']['password']
)

for range_data in provider.get_ranges():
    for ip in ipaddress.IPv4Network(range_data['range']):
        rabbitmq_handler.publish({
            'ip_v4': str(ip),
            'provider': range_data['provider']
        })
