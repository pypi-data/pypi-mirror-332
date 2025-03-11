from uuid import uuid4

from django.conf import settings
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin

# from naval_system.drf.logging import LOCAL


class BaseMiddleware(MiddlewareMixin): # todo

    @classmethod
    def process_request(cls, request):

        LOCAL.remote_ip = request.META.get('HTTP_X_FORWARDED_FOR') or \
                          request.META.get('HTTP_X_REAL_IP') or \
                          request.META.get('REMOTE_ADDR') or ''
        request.request_id = LOCAL.request_id = request.META.get('HTTP_X_REQUEST_ID', str(uuid4()))
        request.start_at = timezone.localtime()

        try:
            body = request.body.decode('utf8')
            body = body[:1000]
            settings.LOGGER.info(f'[request] method:{request.method};path={request.path}', )
            settings.LOGGER.info(f"[request] body:{body}", )
        except:  # noqa
            pass

    def process_response(self, request, response):  # noqa
        try:
            response_content = response.content
        except:  # noqa
            return response
        if len(response_content) > 1000:
            response_content = response_content[:997] + b'...'
        try:
            response_content = response_content.decode('utf8')
        except:  # noqa
            pass

        duration = timezone.localtime() - request.start_at
        settings.LOGGER.info(f'[process_response] status_code:{response.status_code};duration:{duration.seconds}.{duration.microseconds:0>6};content:{response_content}')
        if duration.seconds >= 10:
            settings.LOGGER.info(f'[请求超时] method:{request.method};path={request.path};duration:{duration.seconds}.{duration.microseconds:0>6};{request.request_id=}', )
        return response
