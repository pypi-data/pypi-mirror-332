from django.http import JsonResponse, HttpRequest
from django.utils.deprecation import MiddlewareMixin

class ValarResponse(JsonResponse):
    def __init__(self, data, message='', code='info'):
        self.message = message
        self.code = code
        super(ValarResponse, self).__init__(data, safe=False)


class Middleware(MiddlewareMixin):
    @staticmethod
    def process_response(request: HttpRequest, response: ValarResponse):
        headers = response.headers
        if type(response)==ValarResponse:
            message, code = response.message, response.code
            headers['valar_message'] = message
            headers['valar_code'] = code
        auth = request.headers.get('AUTH')
        if auth:
            headers['auth'] = auth
        uid = request.session.get('UID')
        if uid:
            headers['uid'] = uid
        return response