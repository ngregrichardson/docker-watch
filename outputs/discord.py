import logger
import requests
from datetime import datetime, timedelta
import time

class Output:
    def __init__(self, output_data):
        self.data = output_data
        self.init()
    
    def init(self):
        self.username = self.data.get("username", "Docker Watch")
        self.webhook = self.data.get("webhook", None)
        if self.webhook is None:
            logger.warn("None or invalid \'discord\' webhook.")
        
    def fire_event(self, event_data):
        event_type = event_data.get('Type', None)
        event_action = event_data.get('Action', None)
        event_from = event_data.get('from', None)
        event_time = event_data.get('time', None)

        embed = {
            'fields': [],
            'username': self.username
        }

        if event_action is None or event_action is None or event_type is None:
            embed['title'] = 'Watched Event Fired'
        else:
            embed['title'] = f'{event_action.capitalize()} event fired on the \'{event_from}\' {event_type}'

        if event_time is None:
            timestamp = datetime.now()
        else:
            timestamp = datetime.fromtimestamp(event_time)
        
        offset = time.timezone if (time.localtime().tm_isdst == 0) else time.altzone

        timestamp = timestamp + timedelta(seconds=offset)
        
        embed['timestamp'] = timestamp.isoformat()

        embed['fields'] = [
            {
                'name': 'Type',
                'value': event_type.capitalize(),
                'inline': False
            },
            {
                'name': 'Action',
                'value': event_action.capitalize(),
                'inline': False
            },
            {
                'name': 'From',
                'value': event_from,
                'inline': False
            }
        ]
        
        requests.post(self.webhook, json = { 'embeds': [embed] })