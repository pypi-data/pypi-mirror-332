class KafkaError(Exception):
    """Kafka error"""


class PartitionEndReached(KafkaError):
    """Partition end reached"""


class KafkaBrokerTransportError(Exception):
    """Kafka broker transport error"""


class KafkaTopicNotRegistered(Exception):
    """Kafka topic not registered"""


class SchemaNotFound(Exception):
    """Schema not found"""


class KafkaMessageDeliveryError(KafkaError):
    """Kafka message delivery error"""

    def __init__(self, error: str, message):
        self.error = error
        self.message = message
