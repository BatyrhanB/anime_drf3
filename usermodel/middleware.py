from django.utils.deprecation import MiddlewareMixin
import time

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
        # print("\033[5;37;40m Time view\033[0;37;40m\n", end_time - start_time)
        return response
        
        
