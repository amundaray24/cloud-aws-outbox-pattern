import json

from lambda_utils_logger.logger_util import Logger

from domain.event_action import EventAction, EventActionStatus
from infrastructure.s3.event_dispatcher_bucket_adapter import EventDispatchBucketAdapter
from infrastructure.sns.event_dispatcher_adapter import EventDispatchAdapter
from infrastructure.dynamo.event_dispatcher_dynamo_adapter import EventDispatchDynamoAdapter

logger = Logger().get_logger(__name__)

class EventDispatcherUseCase:

  @staticmethod
  def execute(event_action : EventAction):
    logger.debug(f"EventDispatcherUseCase - execute - event_action: {event_action}")
    logger.info(f"EventDispatcherUseCase - execute - id: {event_action.id}")
    event_content = EventDispatchBucketAdapter().get_objet(s3_key=event_action.current.s3Key)
    if not event_content:
      logger.error(f"EventDispatcherUseCase - execute - id: {event_action.id} - event content not found in s3, in {event_action.current.s3Key}")
      EventDispatcherUseCase._update_status(event_action, EventActionStatus.ERROR, f"event content not found in s3, in {event_action.current.s3Key}")
      return
    EventDispatcherUseCase._update_status(event_action, EventActionStatus.DISPATCHED, None)
    EventDispatchAdapter().dispatch(
      topic=event_action.current.topic,
      message=json.dumps(json.loads(event_content)),
      headers=event_action.current.headers,
      message_group_id=event_action.current.messageGroupId,
      message_deduplication_id=event_action.current.deduplicationId
    )
    logger.info(f"EventDispatcherUseCase - execute - id: {event_action.id} - dispatched")

  @staticmethod
  def _update_status(event_action: EventAction, status: EventActionStatus, reason):
    current_content_for_update = {
      "status": status,
      "reason": reason
    }
    updated_current = event_action.current.copy(update=current_content_for_update)
    updated_event_action = event_action.copy(update={
      "current": updated_current
    })
    EventDispatchDynamoAdapter().update_event_action(updated_event_action)