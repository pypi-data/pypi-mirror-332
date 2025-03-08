import asyncio
import importlib
import json
from django.core.exceptions import ImproperlyConfigured
from django.http import JsonResponse
from django.conf import settings

from src.valar.channels import ValarSocketSender


async def handel_channel(request, handler):
    client = request.headers.get('CLIENT')
    uid = request.session.get('UID')
    data = json.loads(request.body)
    method = get_valar_channel_handler(handler)
    loop = asyncio.get_event_loop()
    sender = ValarSocketSender(handler, client, uid)
    loop.create_task(method(data, sender))
    return JsonResponse({'status':'OK'}, safe=False)




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
