import pika
import json


class RabbitMQHandler:
    channel = None
    queue_name = 'ip_v4_messages'

    def __init__(self, host, username, password):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=host,
                credentials=pika.credentials.PlainCredentials(
                    username=username,
                    password=password
                )
            )
        )

    def set_up_channel(self) -> None:
        if not self.channel:
            self.channel = self.connection.channel()
            self.channel.queue_declare(
                queue=self.queue_name
            )
        pass

    def publish(self, payload) -> None:
        self.set_up_channel()
        self.channel.basic_publish(
            exchange='',
            routing_key=self.queue_name,
            body=json.dumps(payload)
        )

    def consume(self, on_message_callable) -> None:
        self.set_up_channel()
        self.channel.basic_consume(
            queue=self.queue_name,
            on_message_callback=on_message_callable,
            auto_ack=True
        )
        try:
            self.channel.start_consuming()
        except KeyboardInterrupt:
            self.channel.stop_consuming()
        finally:
            self.connection.close()

