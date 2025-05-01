import os
import boto3
from lambda_utils_logger.logger_util import Logger

logger = Logger().get_logger(__name__)

class DynamoUtils:

  _instance = None

  def __new__(cls):
    if cls._instance is None:
      cls._instance = super(DynamoUtils, cls).__new__(cls)
      cls._instance._init()
    return cls._instance

  def _init(self):
    """Initialize the dynamoDb client."""
    self._region = os.environ.get('AWS_REGION', 'eu-central-1')
    self._dynamo_client = boto3.client('dynamodb', region_name=self._region)

  def _validate_table_name(self, table_name):
    try:
      self._dynamo_client.describe_table(TableName=table_name)
    except self._dynamo_client.exceptions.ResourceNotFoundException:
      logger.error(f"Table not found: {table_name}")
      raise Exception(f"Table not found: {table_name}")
    except Exception as e:
      logger.error(f"Error obtaining table: {table_name}. Error: {e}")
      raise e

  def update_item(self, table_name, keys, update_expression, expression_attribute_names, expression_attribute_values ):
    try:
      self._validate_table_name(table_name)
      self._dynamo_client.update_item(
        TableName=table_name,
        Key=keys,
        UpdateExpression=update_expression,
        ExpressionAttributeNames=expression_attribute_names,
        ExpressionAttributeValues=expression_attribute_values
      )
    except Exception as e:
      logger.error(f"Error updating table: {table_name} and keys: {keys}. Error: {e}")
      raise e