import os
import boto3
import json

from lambda_utils_logger.logger_util import Logger

logger = Logger().get_logger(__name__)

class SecretManagerUtil:

  _instance = None

  def __new__(cls):
    if cls._instance is None:
      cls._instance = super(SecretManagerUtil, cls).__new__(cls)
      cls._instance._init()
    return cls._instance

  def _init(self):
    self._region = os.environ.get('AWS_REGION', 'eu-central-1')
    self._account_id = os.environ.get('AWS_ACCOUNT_ID', '000000000000')
    if not self._region or not self._account_id:
      raise ValueError("AWS_REGION and AWS_ACCOUNT_ID must be set in the environment")
    self._secret_manager_client = boto3.client('secretsmanager', region_name=self._region)

  def _build_secret_arn(self, secret_name: str) -> str:
    logger.debug(f"Building secret ARN for secret: {secret_name}")
    return f"arn:aws:secretsmanager:{self._region}:{self._account_id}:secret:{secret_name}"

  def get_secret(self, secret_name: str) -> dict:
    """Retrieve the secret with the specified name"""
    logger.debug(f"Retrieving secret: {secret_name}")
    response = self._secret_manager_client.get_secret_value(SecretId=self._build_secret_arn(secret_name))
    secret = json.loads(response['SecretString'])
    logger.debug(f"Secret retrieved successfully: {json.dumps(secret, indent=2)}")
    return secret