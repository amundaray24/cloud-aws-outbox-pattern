from lambda_utils_logger.logger_util import Logger
from lambda_utils_s3.s3_bucket_util import S3Utils
from lambda_utils_xray.xray_util import XRayUtil
from lambda_utils_sns_dispatcher.sns_dispatcher import SNSDispatcher
from lambda_utils_dynamo_serializer.dynamo_deserializer import DynamoDeserializer

class Configurator:

  _instance = None

  def __new__(cls):
    if cls._instance is None:
      cls._instance = super(Configurator, cls).__new__(cls)
      cls._instance._init()
    return cls._instance

  def _init(self):
    Logger()
    XRayUtil()
    S3Utils()
    SNSDispatcher()
    DynamoDeserializer()


