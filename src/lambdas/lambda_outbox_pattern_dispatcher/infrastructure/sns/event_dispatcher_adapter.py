import json

from lambda_utils_logger.logger_util import Logger
from lambda_utils_sns_dispatcher.sns_dispatcher import SNSDispatcher

logger = Logger().get_logger(__name__)

class EventDispatchAdapter:

  _instance = None

  def __new__(cls, *args, **kwargs):
    if cls._instance is None:
      cls._instance = super(EventDispatchAdapter, cls).__new__(cls, *args, **kwargs)
      cls._instance._init()
    return cls._instance

  def _init(self):
    self._dispatcher = SNSDispatcher()

  def dispatch(self, topic: str, message: str, headers: dict, message_group_id: str, message_deduplication_id: str):
    logger.debug(f"EventDispatcherAdapter topic: {topic}")
    logger.debug(f"EventDispatcherAdapter headers: {headers}")
    logger.debug(f"EventDispatcherAdapter message: {message}")
    logger.debug(f"EventDispatcherAdapter message_group_id: {message_group_id}")
    logger.debug(f"EventDispatcherAdapter message_deduplication_id: {message_deduplication_id}")
    logger.info(f"EventDispatcherAdapter init publish in topic: {topic} with headers: {json.dumps(headers)}")
    self._dispatcher.publish_message(
      sns_topic_name=topic,
      message=message,
      message_attributes=headers,
      message_group_id=message_group_id,
      message_deduplication_id=message_deduplication_id
    )
    logger.debug(f"EventDispatcherAdapter published in topic: {topic}")