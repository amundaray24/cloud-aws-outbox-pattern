from lambda_utils_logger.logger_util import Logger

from domain.event_action import EventAction
from infrastructure.sns.action_split_event_dispatch_adapter import ActionSplitEventDispatchAdapter

logger = Logger().get_logger(__name__)

class ActionSplitUseCase:

  @staticmethod
  def execute(event_action : EventAction):
    logger.info(f"ActionSplitUseCase: {event_action.operation}")
    logger.debug(f"ActionSplitUseCase Request: {event_action}")
    ActionSplitEventDispatchAdapter().dispatch(event_action)
    # TODO: validate if event structure isvalid (internal structure of data)
    logger.debug(f"ActionSplitUseCase dispatched: {event_action}")
    logger.info(f"ActionSplitUseCase: {event_action.operation} executed")

