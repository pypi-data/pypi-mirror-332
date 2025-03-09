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
        message, code = response.message, response.code
        user_id = request.session.get('USER_ID')
        headers = response.headers
        headers['valar_message'] = message
        headers['valar_code'] = code
        if user_id:
            headers['user_id'] = user_id
        return response