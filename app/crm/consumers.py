import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ClientConsumer(WebsocketConsumer):
    def connect(self):

        self.room_group_name = 'realtime_client_wallet'

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    #receieve from websocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['client_data']
        print(message)

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'wallet_data': message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['wallet_data']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'type': 'chat_message',
            'wallet_data': message
        }))