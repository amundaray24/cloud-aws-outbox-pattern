import os

from lambda_utils_logger.logger_util import Logger
from lambda_utils_s3.s3_bucket_util import S3Utils

logger = Logger().get_logger(__name__)

class EventDispatchBucketAdapter:

  _instance = None

  def __new__(cls, *args, **kwargs):
    if cls._instance is None:
      cls._instance = super(EventDispatchBucketAdapter, cls).__new__(cls, *args, **kwargs)
      cls._instance._init()
    return cls._instance

  def _init(self):
    self._dispatcher = S3Utils()
    self._bucket_s3 = os.environ.get('OUTBOX_PATTERN_BUCKET_NAME', 'outbox-pattern-bucket')

  def get_objet(self, s3_key: str):
    logger.info(f"EventDispatchBucketAdapter get_objet - s3_key: {s3_key}")
    content = self._dispatcher.get_file(s3_bucket_name=self._bucket_s3, s3_key=s3_key)
    logger.debug(f"EventDispatchBucketAdapter get_objet - content: {content}")
    logger.info(f"EventDispatchBucketAdapter get_objet - finish")
    return content
