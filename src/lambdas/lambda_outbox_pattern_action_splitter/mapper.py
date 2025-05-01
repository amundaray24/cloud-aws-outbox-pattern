from domain.event_action import EventAction

from lambda_utils_dynamo_serializer.dynamo_deserializer import DynamoDeserializer

class Mapper:

    @staticmethod
    def map(event: dict) -> EventAction:
      event_body = DynamoDeserializer().deserialize(event['dynamodb'])
      record = {
        "id": event_body.get('Keys', {}).get('id'),
        "operation": event.get('eventName')
      }
      if 'NewImage' in event_body:
        record['current'] = event_body['NewImage']
      if 'OldImage' in event_body:
        record['previous'] = event_body['OldImage']
      return EventAction(**record)