from django.utils.deprecation import MiddlewareMixin

class CustomXFrameOptionsMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if 'allow_iframe' in request.path:
            response['X-Frame-Options'] = 'ALLOWALL'
        else:
            response['X-Frame-Options'] = 'DENY'
        return response
