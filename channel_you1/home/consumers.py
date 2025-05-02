from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class TestConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = "test_consumer"
        self.room_group_name = "test_consumer_group"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        self.send(text_data=json.dumps({'status': 'connected channels'}))

    # Receive message from WebSocket
    def receive(self, text_data):
        print(text_data)
        self.send(text_data=json.dumps(text_data))
        pass


    def disconnect(self, *args, **kwargs):
        print('disconnect')
        pass

    # Receive message from room group
    def send_notification(self, event):
        print('send notification')
        print(event.get('value'))
        self.send(text_data=json.dumps({'payload': event.get('value')}))
        print('send notification')