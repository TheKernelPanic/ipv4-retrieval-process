import os

from dotenv import load_dotenv

load_dotenv()

parameters = {
    'database': {
        'host': os.getenv('POSTGRES_HOST'),
        'username': os.getenv('POSTGRES_USERNAME'),
        'password': os.getenv('POSTGRES_PASSWORD'),
        'name': os.getenv('POSTGRES_DATABASE_NAME')
    },
    'rabbitmq': {
        'host': os.getenv('RABBITMQ_HOST'),
        'username': os.getenv('RABBITMQ_USERNAME'),
        'password': os.getenv('RABBITMQ_PASSWORD')
    }
}
