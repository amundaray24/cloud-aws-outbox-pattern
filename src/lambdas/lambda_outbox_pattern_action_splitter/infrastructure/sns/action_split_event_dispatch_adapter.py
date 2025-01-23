import os
import uuid
import json

from datetime import datetime

from domain.event_action import EventAction

from lambda_utils_logger.logger_util import Logger
from lambda_utils_sns_dispatcher.sns_dispatcher import SNSDispatcher

logger = Logger().get_logger(__name__)

class ActionSplitEventDispatchAdapter:

  _instance = None

  def __new__(cls, *args, **kwargs):
    if cls._instance is None:
      cls._instance = super(ActionSplitEventDispatchAdapter, cls).__new__(cls, *args, **kwargs)
      cls._instance._init()
    return cls._instance

  def _init(self):
    self._dispatcher = SNSDispatcher()
    self._topic_name = os.environ.get('APP_ACTION_SPLITTER_SNS_TOPIC_NAME', 'app-action-splitter-sns-topic')

  def dispatch(self, event_action: EventAction):
    logger.debug(f"ActionSplitEventDispatchAdapter: {event_action.operation}")
    logger.info(f'ActionSplitEventDispatchAdapter: dispatching event to SNS topic: {self._topic_name}')
    headers = {
      "eventDate": str(datetime.now().isoformat()),
      "operation": event_action.operation
    }
    self._dispatcher.publish_message(
      sns_topic_name=self._topic_name,
      message=json.dumps(event_action.data),
      message_attributes=headers,
      message_group_id=event_action.operation,
      message_deduplication_id=str(uuid.uuid4())
    )
    logger.debug(f"ActionSplitEventDispatchAdapter: {event_action.operation} dispatched")