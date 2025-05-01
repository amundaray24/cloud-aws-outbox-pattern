import json

from lambda_utils_logger.logger_util import Logger
from lambda_utils_xray.xray_util import XRayUtil

logger = Logger().get_logger("event_base_handler")
xray_util = XRayUtil()

class EventsBaseHandler:
  def __init__(self, use_case, mapper):
    self.use_case = use_case
    self.mapper = mapper

  def handler(self, event, context):
      if event is None or 'Records' not in event or len(event['Records']) == 0:
          logger.info("empty event batch execution")
          raise Exception("empty event batch execution")
      logger.info(f"init event batch execution size: {len(event['Records'])}")
      logger.debug(f"Received event: {json.dumps(event, indent=2)}")
      for record in event['Records']:
          self._process_record(record)
      logger.info("end event batch execution")
      return {"statusCode": 200}

  def _process_record(self, event):
      try:
          logger.info(f"Processing record")
          logger.debug(f"Processing record: {json.dumps(event, indent=2)}")
          xray_util.create_new_subsegment("process_record")
          logger.debug(f"Event action: {event}")
          self.use_case.execute(self.mapper.map(event))
          logger.info(f"Record processed successfully")
      except Exception as e:
          logger.error(f"Error processing record: {e}")
          raise e
      finally:
          xray_util.end_subsegment()