from datetime import datetime

from channels.layers import get_channel_layer

from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.conf import settings

try:
    GROUP = settings.VALAR_CHANNEL_GROUP_NAME
except AttributeError:
    GROUP = 'VALAR'

class ValarSocketSender:
    def __init__(self, handler: str, client: str, uid):
        self.client = client
        self.uid = uid
        self.handler = handler
        self.send = get_channel_layer().group_send

    def __convert_body(self, emit, data ,clients = None, users = None):
        return {
            'type': emit,
            'data': {
                'handler': self.handler,
                'payload': data,
                'timestamp': datetime.now().timestamp()
            },
            'clients': clients or [],
            'users': users or [],
        }


    async def to_users(self, data, *users):
        body = self.__convert_body('user.emit', data, users=users)
        await self.send(GROUP, body)

    async def to_clients(self,data, *clients):
        body = self.__convert_body('client.emit', data, clients=clients)
        await self.send(GROUP, body)

    async def broadcast(self, data):
        body = self.__convert_body('broadcast.emit', data)
        await self.send(GROUP, body)

    async def register(self):
        body = self.__convert_body('register.emit',  [self.client], [self.uid])
        await self.send(GROUP, body)


class ValarConsumer(AsyncJsonWebsocketConsumer):

    def __init__(self):
        self.client = None
        self.uid = None
        super().__init__()

    async def connect(self):
        params = self.scope['url_route']['kwargs']
        self.client = params.get('client')
        await self.channel_layer.group_add(GROUP, self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(GROUP, self.channel_name)
        await self.close(code)

    async def receive_json(self, data, *args, **kwargs):
        print(data)
        pass

    async def user_emit(self, event):
        users: list = event.get('users',[])
        data = event.get('data',{})
        if self.uid in users:
            await self.send_json(data)


    async def client_emit(self, event):
        clients: list = event.get('clients',[])
        data = event.get('data',{})
        if self.client in clients:
            await self.send_json(data)

    async def broadcast_emit(self, event):
        data = event.get('data',{})
        await self.send_json(data)

    async def register_emit(self, event):
        users: list = event.get('users', [])
        clients: list = event.get('clients',[])
        if self.client in clients:
            self.uid = users[0]










