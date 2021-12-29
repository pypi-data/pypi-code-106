import json

from confluent_kafka import Consumer as CKConsumer
from confluent_kafka import Producer as CKProducer
from confluent_kafka import KafkaError
from confluent_kafka import KafkaException

from skeleton.monitoring import LoggerMixin


class BaseKafkaProducer(object):
    @staticmethod
    def value_serializer(value):
        return json.dumps(value).encode('utf-8')

    def produce(self,
                topic,
                value,
                *args,
                **kwargs):
        """
        Produce {value} to {topic}.
        """
        raise NotImplementedError


class BaseKafkaConsumer(object):
    @staticmethod
    def value_deserializer(value):
        return json.loads(value.decode('utf-8'))

    def consume(self,
                on_message,
                poll_timeout,
                *args,
                **kwargs):
        """
        Consume loop.
        """
        raise NotImplementedError

    def process_message(self,
                        message,
                        *args,
                        **kwargs):
        """
        Process {message}.
        """
        raise NotImplementedError


class ConfluentProducer(BaseKafkaProducer):
    def __init__(self,
                 config,
                 *args,
                 **kwargs):
        self._kafka_producer = CKProducer(config)

    def produce(self,
                topic,
                value,
                *args,
                **kwargs):
        self._kafka_producer.produce(topic=topic,
                                     value=value,
                                     *args,
                                     **kwargs)

    def producer_poll(self,
                      timeout=0):
        """
        Polls the producer for events and calls the corresponding callbacks (if registered).
        """
        self._kafka_producer.poll(timeout=timeout)

    def flush(self,
              timeout=60):
        """
        Wait for all messages in the queue to be delivered.
        """
        self._kafka_producer.flush(timeout=timeout)


class ConfluentConsumer(BaseKafkaConsumer):
    def __init__(self,
                 config,
                 *args,
                 **kwargs):
        self._kafka_consumer = CKConsumer(config)

    def subscribe(self,
                  topics,
                  *args,
                  **kwargs):
        """
        Set subscription to supplied list of topics.
        This replaces a previous subscription.
        """
        self._kafka_consumer.subscribe(topics=topics)

    def consumer_poll(self,
                      timeout=None):
        """
        Consumes a single message, calls callbacks and returns events.
        """
        return self._kafka_consumer.poll(timeout=timeout)

    def close(self):
        """
        Close down and terminate the Kafka Consumer.
        """
        self._kafka_consumer.close()

    def consume(self,
                on_message,
                poll_timeout=None):
        while True:
            msg = self.consumer_poll(timeout=poll_timeout)

            if msg is None:
                # No message available within timeout.
                # Initial message consumption may take up to
                # `session.timeout.ms` for the consumer group to
                # rebalance and start consuming
                continue

            on_message(msg)


class Producer(ConfluentProducer,
               LoggerMixin):
    def __init__(self,
                 config):
        self.logger.info(f'KAFKA PRODUCER: CONNECTING {config.get("bootstrap.servers")} ...')
        super().__init__(config)

    def produce(self,
                topic,
                value,
                *args,
                **kwargs):
        value = self.value_serializer(value=value)
        self.logger.info(f'KAFKA PRODUCER: PRODUCING {value} TO TOPIC {topic}')
        super().produce(topic=topic,
                        value=value,
                        *args,
                        **kwargs)


class Consumer(ConfluentConsumer,
               LoggerMixin):
    def __init__(self,
                 config):
        bootstrap_servers = config.get('bootstrap.servers')
        group_id = config.get('group.id')
        self.logger.info(f'KAFKA CONSUMER: CONNECTING {bootstrap_servers} ... AS MEMBER OF {group_id}')
        super().__init__(config)

    def on_message(self,
                   msg):
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                log = f'KAFKA CONSUMER: {msg.topic()} [{msg.partition()}] REACHED END AT OFFSET {msg.offset()}'
                self.logger.error(log)
            else:
                raise KafkaException(msg.error())
        else:
            self.logger.info(f'KAFKA CONSUMER: PROCESSING [{msg.partition()}]:{msg.offset()}:{msg.timestamp()}')
            value = self.value_deserializer(msg.value())
            self.process_message(message=value)

    def consume(self,
                topics,
                timeout=1.0):
        try:
            self.subscribe(topics)
            self.logger.info(f'KAFKA CONSUMER: STARTED CONSUMING OF TOPICS {topics} WITH TIMEOUT={timeout}')

            super().consume(on_message=lambda m: self.on_message(msg=m),
                            poll_timeout=1.0)
        except KeyboardInterrupt:
            self.logger.warning('KAFKA CONSUMER: KEYBOARD INTERRUPT')
        finally:
            self.logger.info('KAFKA CONSUMER: CLOSING...')
            self.close()
