import asyncio
import importlib
import json
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings

from .. import ValarResponse
from ..channels import ValarSocketSender


async def handel_channel(request, handler):
    client = request.headers.get('CLIENT')
    auth = request.headers.get('AUTH')
    uid = request.session.get('UID')
    if auth and not uid:
        return ValarResponse(False)
    data = json.loads(request.body)
    try:
        method = get_valar_channel_handler(handler)
    except ImproperlyConfigured:
        return ValarResponse(False, message="Invalid channel handler %r" % handler, code='error')
    sender = ValarSocketSender(handler, client, uid)
    if uid and client:
        await sender.register()
    thread = asyncio.to_thread(method,data, sender)
    asyncio.create_task(thread)
    return ValarResponse(True)




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
