import uuid
import boto3
import json
import os

from src.utils.lambda_utils_xray import xray_formatter, xray_util
from src.utils.lambda_utils_logger import  logger

REGION = os.environ['AWS_REGION']
ACCOUNT_ID = os.environ['AWS_ACCOUNT_ID']
SNS_TOPIC_NAME = os.environ['APP_ACTION_SPLITTER_SNS_TOPIC_NAME']

sns = boto3.client('sns', region_name=REGION)
log = logger.build_logger_custom("ActionSplitter", xray_formatter.XRayFormatter('[%(asctime)s] [%(levelname)s] [trace_id=%(trace_id)s span_id=%(span_id)s] %(message)s'))

def get_sns_topic_arn():
    return f"arn:aws:sns:{REGION}:{ACCOUNT_ID}:{SNS_TOPIC_NAME}"

def handler(event, context):
    log.debug(f"Received event: {json.dumps(event, indent=2)}")
    for record in event['Records']:
        try:
            xray_util.create_new_subsegment("process_record")
            sns_topic_arn = get_sns_topic_arn()
            operation_type = record['eventName']
            log.info(f"Operation type: {operation_type}")
            message = {
                "operation": operation_type,
                "data": record['dynamodb']
            }
            log.debug(f"Publishing message: {json.dumps(message)}")
            sns.publish(
                TopicArn=sns_topic_arn,
                Message=json.dumps(message),
                MessageDeduplicationId=str(uuid.uuid4()),
                MessageGroupId=str(uuid.uuid4()),
                MessageAttributes={
                    "operation": {
                        "DataType": "String",
                        "StringValue": operation_type
                    }
                }
            )
        except Exception as e:
            log.error(f"Error processing record: {e}")
            raise e
        finally:
            xray_util.end_subsegment()
    return {"statusCode": 200}