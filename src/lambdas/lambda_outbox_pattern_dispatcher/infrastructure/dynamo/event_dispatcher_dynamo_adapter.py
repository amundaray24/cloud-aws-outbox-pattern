from datetime import datetime, timezone

from domain.event_action import EventAction
from lambda_utils_logger.logger_util import Logger
from lambda_utils_dynamo.dynamo_table_util import DynamoUtils

logger = Logger().get_logger(__name__)

class EventDispatchDynamoAdapter:

  _instance = None

  def __new__(cls, *args, **kwargs):
    if cls._instance is None:
      cls._instance = super(EventDispatchDynamoAdapter, cls).__new__(cls, *args, **kwargs)
      cls._instance._init()
    return cls._instance

  def _init(self):
    self._dynamo_util = DynamoUtils()

  def update_event_action(self, event_action : EventAction):
    logger.debug(f"EventDispatchDynamoAdapter - set_event_dispatched - event_action: {event_action}")
    logger.info(f"EventDispatchDynamoAdapter - set_event_dispatched - id: {event_action.current.id}")

    keys = {
      "id": {
        "S": str(event_action.current.id)
      },
      "created_at": {
        "S": str(event_action.current.createdAt)
      }
    }

    if event_action.current.reason:
      update_expression = "SET #status = :status, #reason = :reason, #last_updated_at = :last_updated_at"
      expression_attribute_names = {
        "#status": "status",
        "#reason": "reason",
        "#last_updated_at": "last_updated_at"
      }
      expression_attribute_values = {
        ":status": {
          "S": str(event_action.current.status)
        },
        ":reason": {
          "S": str(event_action.current.reason)
        },
        ":last_updated_at": {
          "S": datetime.now(timezone.utc).isoformat()
        }
      }
    else:
      update_expression = "SET #status = :status, #last_updated_at = :last_updated_at"
      expression_attribute_names = {
        "#status": "status",
        "#last_updated_at": "last_updated_at"
      }
      expression_attribute_values = {
        ":status": {
          "S": str(event_action.current.status)
        },
        ":last_updated_at": {
          "S": datetime.now(timezone.utc).isoformat()
        }
      }

    self._dynamo_util.update_item(
      table_name='monkey-euc1-dynamo-outbox-pattern',
      keys = keys,
      update_expression = update_expression,
      expression_attribute_names = expression_attribute_names,
      expression_attribute_values = expression_attribute_values
    )
    logger.info(f"EventDispatchDynamoAdapter - set_event_dispatched - id: {event_action.current.id} - dispatched")