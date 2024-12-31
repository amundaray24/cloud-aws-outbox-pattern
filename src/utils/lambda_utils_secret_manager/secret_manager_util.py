import os
import boto3
import json
import logging


class SecretManagerUtil:

  def __init__(self, logger: logging.Logger, region: str = None, account_id: str = None):
    self.logger = logger
    self.region = region or os.environ.get('AWS_REGION')
    self.account_id = account_id or os.environ.get('AWS_ACCOUNT_ID')
    self.secrets_manager = boto3.client('secretsmanager', region_name=self.region)

  def _build_secret_arn(self, secret_name: str) -> str:
    self.logger.debug(f"Building secret ARN for secret: {secret_name}")
    return f"arn:aws:secretsmanager:{self.region}:{self.account_id}:secret:{secret_name}"

  def get_secret(self, secret_name: str) -> dict:
    """Retrieve the secret with the specified name"""
    self.logger.debug(f"Retrieving secret: {secret_name}")
    response = self.secrets_manager.get_secret_value(SecretId=self._build_secret_arn(secret_name))
    secret = json.loads(response['SecretString'])
    self.logger.debug(f"Secret retrieved successfully: {json.dumps(secret, indent=2)}")
    return secret