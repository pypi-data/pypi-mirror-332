import asyncio
import importlib
import json
from datetime import datetime

from channels.layers import get_channel_layer

from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.core.exceptions import ImproperlyConfigured
from django.http import JsonResponse
from django.conf import settings

GROUP = 'VALAR'

class ValarSocketSender:
    def __init__(self, data: dict, handler: str, message = None, code = None):
        self.data = data
        self.handler = handler
        self.send = get_channel_layer().group_send
        self.message = message
        self.code = code

    def __convert_body(self, emit, clients = None, users = None):
        return {
            'type': emit,
            'data': {
                'handler': self.handler,
                'payload': self.data,
                'message': self.message,
                'type': self.code,
                'timestamp': datetime.now().timestamp()
            },
            'clients': clients or [],
            'users': users or [],
        }

    async def set_message(self, message, code):
        self.message = message
        self.code = code

    async def to_users(self, *users):
        body = self.__convert_body('user.emit', users=users)
        await self.send(GROUP, body)

    async def to_clients(self, *clients):
        body = self.__convert_body('client.emit', clients=clients)
        await self.send(GROUP, body)

    async def broadcast(self):
        body = self.__convert_body('broadcast.emit')
        await self.send(GROUP, body)

    async def register(self, client, uid):
        body = self.__convert_body('register.emit',  [client], [uid])
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



def get_valar_channel_handler(handler):
    try:
        root = settings.VALAR_CHANNEL_HANDLER_MAPPING
        path, name = root.rsplit(".", 1)
    except (ValueError, AttributeError):
        raise ImproperlyConfigured("Cannot find VALAR_CHANNEL_HANDLER_MAPPING setting.")
    try:
        module = importlib.import_module(path)
        mapping = getattr(module, name)
    except ImportError:
        raise ImproperlyConfigured("Cannot import VALAR_CHANNEL_HANDLER_MAPPING module %r" % path)
    except AttributeError:
        raise ImproperlyConfigured("module %r has no attribute %r" % (path, name))
    try:
        method = mapping[handler]
    except KeyError:
        raise ImproperlyConfigured("Cannot find handler in %r" % root)
    return method




async def socket(request, handler):
    client = request.headers.get('CLIENT')
    uid = request.session.get('UID')
    data = json.loads(request.body)
    method = get_valar_channel_handler(handler)
    loop = asyncio.get_event_loop()
    loop.create_task(method(data, handler, client, uid))
    return JsonResponse({'status':'OK'}, safe=False)


