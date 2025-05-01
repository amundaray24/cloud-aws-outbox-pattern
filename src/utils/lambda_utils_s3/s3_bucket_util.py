import os
import boto3
from lambda_utils_logger.logger_util import Logger

logger = Logger().get_logger(__name__)

class S3Utils:

  _instance = None

  def __new__(cls):
    if cls._instance is None:
      cls._instance = super(S3Utils, cls).__new__(cls)
      cls._instance._init()
    return cls._instance

  def _init(self):
    """Initialize the s3 client."""
    self._region = os.environ.get('AWS_REGION', 'eu-central-1')
    self._account_id = os.environ.get('AWS_ACCOUNT_ID', '000000000000')
    if not self._region or not self._account_id:
      raise ValueError("AWS_REGION and AWS_ACCOUNT_ID must be set in the environment")
    self._s3_client = boto3.client('s3', region_name=self._region)

  def get_file(self, s3_bucket_name, s3_key):
    if not self._exist_file(s3_bucket_name, s3_key):
      logger.error(f"File not found in s3: {s3_key}")
      return None
    response = self._s3_client.get_object(Bucket=s3_bucket_name, Key=s3_key)
    file_content = response['Body'].read().decode('utf-8')
    return file_content

  def _exist_file(self, s3_bucket_name, s3_key):
    try:
      self._s3_client.head_object(Bucket=s3_bucket_name, Key=s3_key)
      return True
    except Exception as e:
      logger.error(f"Error checking if file exists: {e}")
      return False