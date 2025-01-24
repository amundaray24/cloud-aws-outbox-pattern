import json

from lambda_utils_logger.logger_util import Logger
from lambda_utils_xray.xray_util import XRayUtil
from lambda_utils_dynamo_serializer.dynamo_deserializer import DynamoDeserializer

from configurator import Configurator
from domain.event_action import EventAction
from application.action_split_use_case import ActionSplitUseCase

logger = Logger().get_logger("lambda_outbox_pattern_action_splitter")
xray_util = XRayUtil()
Configurator()

def handler(event, context):
  if event is None or 'Records' not in event or len(event['Records']) == 0:
    logger.info("empty event batch execution")
    return {"statusCode": 200}
  logger.info(f"init event batch execution size: {len(event['Records'])}")
  logger.debug(f"Received event: {json.dumps(event, indent=2)}")
  for record in event['Records']:
    _process_record(record)
  logger.info("end event batch execution")
  return {"statusCode": 200}

def _process_record(record):
  try:
    logger.info(f"Processing record")
    logger.debug(f"Processing record: {json.dumps(record, indent=2)}")
    xray_util.create_new_subsegment("process_record")
    event_action = _map_record(record)
    logger.debug(f"Event action: {event_action}")
    ActionSplitUseCase.execute(event_action)
    logger.info(f"Record processed successfully")
  except Exception as e:
    logger.error(f"Error processing record: {e}")
    raise e
  finally:
    xray_util.end_subsegment()

def _map_record(record):
  event = DynamoDeserializer().deserialize(record['dynamodb'])
  record = {
    "id": event.get('Keys', {}).get('id'),
    "operation": record.get('eventName')
  }
  if 'NewImage' in event:
    record['current'] = event['NewImage']
  if 'OldImage' in event:
    record['previous'] = event['OldImage']
  return EventAction(**record)