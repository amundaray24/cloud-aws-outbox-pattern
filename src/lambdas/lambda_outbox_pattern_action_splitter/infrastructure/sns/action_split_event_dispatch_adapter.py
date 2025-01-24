import os
import uuid

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

  def dispatch(self, event_action: EventAction, headers: dict):
    logger.debug(f"ActionSplitEventDispatchAdapter: {event_action.operation}")
    logger.info(f'ActionSplitEventDispatchAdapter: dispatching event to SNS topic: {self._topic_name}')
    self._dispatcher.publish_message(
      sns_topic_name=self._topic_name,
      message=event_action.model_dump_json(exclude_none=True),
      message_attributes=headers,
      message_group_id=event_action.operation,
      message_deduplication_id=str(uuid.uuid4())
    )
    logger.debug(f"ActionSplitEventDispatchAdapter: {event_action.operation} dispatched")