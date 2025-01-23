import os
import boto3

from lambda_utils_logger.logger_util import Logger

logger = Logger().get_logger(__name__)

class SNSDispatcher:
  _instance = None

  def __new__(cls):
    if cls._instance is None:
      cls._instance = super(SNSDispatcher, cls).__new__(cls)
      cls._instance._init()
    return cls._instance

  def _init(self):
    """Initialize the SNS client."""
    self._region = os.environ.get('AWS_REGION', 'eu-central-1')
    self._account_id = os.environ.get('AWS_ACCOUNT_ID', '000000000000')
    if not self._region or not self._account_id:
      raise ValueError("AWS_REGION and AWS_ACCOUNT_ID must be set in the environment")
    self._sns_client = boto3.client('sns', region_name=self._region)

  def _get_sns_topic_arn(self, sns_topic_name):
    return f"arn:aws:sns:{self._region}:{self._account_id}:{sns_topic_name}"

  def publish_message(self, sns_topic_name, message, message_attributes=None, message_group_id=None, message_deduplication_id=None):

    logger.info(f"Publishing message to SNS topic: {sns_topic_name}, messageAttributes: {message_attributes}")
    logger.debug(f"Message: {message}")

    if message_attributes and len(message_attributes) > 10:
      raise ValueError("Message attributes cannot exceed 10 in number")

    sns_topic_arn = self._get_sns_topic_arn(sns_topic_name)
    publish_params = {
      "TopicArn": sns_topic_arn,
      "Message": message
    }

    if message_attributes:
      headersValues = {}
      for key, value in message_attributes.items():
        headersValues[key] = {
          "DataType": "String",
          "StringValue": value
        }
      publish_params["MessageAttributes"] = headersValues

    if message_group_id:
      publish_params["MessageGroupId"] = message_group_id

    if message_deduplication_id:
      publish_params["MessageDeduplicationId"] = message_deduplication_id

    self._sns_client.publish(**publish_params)

    logger.info(f"Message published successfully to SNS topic: {sns_topic_name}")
