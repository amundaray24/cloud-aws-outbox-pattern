import json

from domain.event_action import EventAction

class Mapper:

    @staticmethod
    def map(event: dict) -> EventAction:
        payload = json.loads(event['body'])
        return EventAction(**payload)