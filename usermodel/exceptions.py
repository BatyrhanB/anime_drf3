from config.exceptions import BaseException
from rest_framework import status, exceptions


class UserNotVerified(BaseException):
    default_detail = 'user not verified'
    status_code = status.HTTP_406_NOT_ACCEPTABLE
    default_code = 'user_not_virified'
