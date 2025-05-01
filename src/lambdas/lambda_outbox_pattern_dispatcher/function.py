from lambda_utils_handlers.events_base_handler import EventsBaseHandler
from lambda_utils_logger.logger_util import Logger
from lambda_utils_xray.xray_util import XRayUtil

from configurator import Configurator
from mapper import Mapper
from application.event_dispatcher_user_case import EventDispatcherUseCase

logger = Logger().get_logger("lambda_outbox_pattern_dispatcher")
xray_util = XRayUtil()
Configurator()

class LambdaOutboxPatternDispatcher(EventsBaseHandler):

  def __init__(self):
    super().__init__(EventDispatcherUseCase,Mapper)

def handler(event, context):
  dispatcher = LambdaOutboxPatternDispatcher()
  return dispatcher.handler(event, context)