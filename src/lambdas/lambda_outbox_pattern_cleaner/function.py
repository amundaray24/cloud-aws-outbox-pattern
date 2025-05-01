from lambda_utils_handlers.events_base_handler import EventsBaseHandler
from lambda_utils_logger.logger_util import Logger
from lambda_utils_xray.xray_util import XRayUtil

from configurator import Configurator
from mapper import Mapper
from application.cleaner_use_case import CleanerUseCase

logger = Logger().get_logger("lambda_outbox_pattern_cleaner")
xray_util = XRayUtil()
Configurator()

class LambdaOutboxPatternCleaner(EventsBaseHandler):

  def __init__(self):
    super().__init__(CleanerUseCase, Mapper)

def handler(event, context):
  dispatcher = LambdaOutboxPatternCleaner()
  return dispatcher.handler(event, context)