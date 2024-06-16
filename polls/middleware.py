import logging
from django.utils.timezone import now

logger = logging.getLogger(__name__)

class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        user = request.user if request.user.is_authenticated else 'Аноним'
        logger.info(f'{now()} - {user} Посетил {request.path}')
        
        return response
