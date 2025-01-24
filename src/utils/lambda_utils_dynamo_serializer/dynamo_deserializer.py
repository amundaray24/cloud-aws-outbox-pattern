from boto3.dynamodb.types import TypeDeserializer
from lambda_utils_logger.logger_util import Logger

logger = Logger().get_logger(__name__)

class DynamoDeserializer:

  _instance = None

  def __new__(cls):
    if cls._instance is None:
      cls._instance = super(DynamoDeserializer, cls).__new__(cls)
      cls._instance._init()
    return cls._instance

  def _init(self):
    self._type_deserializer = TypeDeserializer()

  def deserialize(self, data):
    if isinstance(data, list):
      return [self.deserialize(v) for v in data]

    if isinstance(data, dict):
      try:
        return self._type_deserializer.deserialize(data)
      except TypeError:
        return {k: self.deserialize(v) for k, v in data.items()}
    else:
      return data