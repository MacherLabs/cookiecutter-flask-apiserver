import logging
logger = logging.getLogger(__name__)
logger.info("Loaded " + __name__)


from {{ cookiecutter.repo_name.replace('-','_') }} import app

from eazyserver.core.kafka_connector import KafkaConnector
from .core.{{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }} import {{ cookiecutter.project_name.capitalize().replace(' ', '').replace('-', '') }}

config = dict(app.config)
behaviour = KafkaConnector(
    {{ cookiecutter.project_name.capitalize().replace(' ', '').replace('-', '') }}(config['BEHAVIOUR_CONFIG']), 
    producer_topic=config['KAFKA_PRODUCER'], 
    consumer_topic=config['KAFKA_CONSUMER'], 
    consumer_topic2=config['KAFKA_CONSUMER_2'], 
    kafka_broker=config['KAFKA_BROKER'],
    sync_consumer=config['KAFKA_SYNC_CONSUMER'])

behaviour.run()

