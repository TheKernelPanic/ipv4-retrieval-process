import sys
from retrieval.prefixes import PrefixesFileReader
import ipaddress
from messages.rabbitmq import RabbitMQHandler
from configuration import parameters

if len(sys.argv) == 1:
    raise Exception('Missing argument')

rabbitmq_handler = RabbitMQHandler(
    host=parameters['rabbitmq']['host'],
    username=parameters['rabbitmq']['username'],
    password=parameters['rabbitmq']['password']
)

elements = PrefixesFileReader().get_ranges_from_file(filename=sys.argv[1].lower())

for element in elements:
    for ip in ipaddress.IPv4Network(element['ip_prefix']):
        print(element)
        rabbitmq_handler.publish({
            'ip_v4': str(ip),
            'provider': element['provider']
        })
