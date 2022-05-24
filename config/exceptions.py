from rest_framework.exceptions import APIException


class BaseException(APIException):
    def __init__(self, detail=None, code=None, status=None):
        if status:
            self.status_code = status
        super().__init__(detail, code)
