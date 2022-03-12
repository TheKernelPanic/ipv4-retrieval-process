import sys
from retrieval.prefixes import PrefixesFileReader
import ipaddress
from messages.rabbitmq import RabbitMQHandler
from configuration import parameters
from utils.logger import Logger

logger = Logger(log_directory=parameters['logging']['directory']).get_logger()

if len(sys.argv) == 1:
    raise Exception('Missing argument')

rabbitmq_handler = RabbitMQHandler(
    host=parameters['rabbitmq']['host'],
    username=parameters['rabbitmq']['username'],
    password=parameters['rabbitmq']['password']
)

elements = PrefixesFileReader().get_ranges_from_file(filename=sys.argv[1].lower())

for element in elements:
    ip_addresses = ipaddress.IPv4Network(element['ip_prefix'])
    total_to_process = ip_addresses.num_addresses
    amount_processed = 1
    for ip in ip_addresses:
        rabbitmq_handler.publish({
            'ip_v4': str(ip),
            'provider': element['provider']
        })
        print(f'Sending {amount_processed}/{total_to_process} of ' + element['ip_prefix'])
        amount_processed += 1
    logger.info('Processed prefix [' + element['ip_prefix'] + '] successfully')