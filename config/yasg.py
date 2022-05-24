from drf_yasg2 import openapi
from drf_yasg2.views import get_schema_view
from rest_framework import permissions
from django.urls import path, include

schema_view = get_schema_view(
    openapi.Info(
        title="Anime API",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]