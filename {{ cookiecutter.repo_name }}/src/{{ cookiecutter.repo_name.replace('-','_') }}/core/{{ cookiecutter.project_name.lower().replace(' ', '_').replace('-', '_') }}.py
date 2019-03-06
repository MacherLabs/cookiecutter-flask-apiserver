import logging
logger = logging.getLogger(__name__)
logger.info("Loaded " + __name__)

from bson.objectid import ObjectId
from eazyserver.core.behaviour_base import Behaviour

class {{ cookiecutter.project_name.capitalize().replace(' ', '').replace('-', '') }}(Behaviour):
    def __init__(self, Config):
        super({{ cookiecutter.project_name.capitalize().replace(' ', '').replace('-', '') }},  self).__init__(Config)
        self.config = Config
        
    def run(self, data, params):
        self.res['_id'] = str(ObjectId())
        self.res['timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.res['producer'] = self.id

        return(self.res)

