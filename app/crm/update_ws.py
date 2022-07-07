from __future__ import absolute_import, unicode_literals
from celery import shared_task
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import json

@shared_task
def update_websocket(new_total):

    channel_layer = get_channel_layer() 

    message = {'type': 'chat_message',
               'wallet_data': str(new_total)}

    async_to_sync(channel_layer.group_send)('realtime_client_wallet', message)