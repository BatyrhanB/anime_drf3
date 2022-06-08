import time
from .models import User
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin
from django.core.cache import cache
from django.views.decorators.cache import cache_page

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# class ScoreRequestsMiddlewere(object):
#     def __init__(self, get_response):
#         super().__init__(get_response)

    # def process_request(self, request):
    #     pass

    # def process_response(self, request, response):
    #     return response


class TimerMiddlewere(MiddlewareMixin):
    def __init__(self, get_response):
        super().__init__(get_response)

    def __call__(self, request, *args, **kwargs):
        start_time = time.monotonic()
        response = self.get_response(request, *args, **kwargs)
        end_time = time.monotonic()
        print(bcolors.OKGREEN + "Time view", end_time - start_time)
        return response
        
        
def set_last_active_middleware(get_response):

    # @cache_page(60*5)
    def middleware(request):
        response = get_response(request)
        if request.user:
            last_active = cache.get('last_active')
            if not last_active:
                User.objects.filter(id=request.user.id).update(last_active=timezone.now())
                cache.set('last_active', last_active, 60)
        return response
    return middleware

