from django.utils.decorators import decorator_from_middleware

from .middleware import RequestLogMiddleware


class RequestLogViewMixin(object):

    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super(RequestLogViewMixin, cls).as_view(*args, **kwargs)
        view = decorator_from_middleware(RequestLogMiddleware)(view)
        return view