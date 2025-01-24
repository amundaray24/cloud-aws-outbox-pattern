from datetime import datetime, timezone

from lambda_utils_logger.logger_util import Logger

from domain.event_action import EventAction
from infrastructure.sns.action_split_event_dispatch_adapter import ActionSplitEventDispatchAdapter

logger = Logger().get_logger(__name__)

class ActionSplitUseCase:

  @staticmethod
  def execute(event_action : EventAction):
    logger.info(f"ActionSplitUseCase: {event_action.operation}")
    logger.debug(f"ActionSplitUseCase Request: {event_action}")
    if event_action.current is None and event_action.previous is None:
      logger.error(f"ActionSplitUseCase: {event_action.operation} invalid request, both current and previous are None")
      return
    headers = {
      "eventDate": str(datetime.now(timezone.utc).isoformat()),
      "operation": event_action.operation
    }

    if event_action.current is not None:
      headers["currentStatus"] = str(event_action.current.status)

    if event_action.previous is not None:
      headers["previousStatus"] = str(event_action.previous.status)

    ActionSplitEventDispatchAdapter().dispatch(event_action, headers)
    logger.debug(f"ActionSplitUseCase dispatched: {event_action}")
    logger.info(f"ActionSplitUseCase: {event_action.operation} executed")

