import environ
from django.urls import path, re_path, include
from drf_yasg2 import openapi
from drf_yasg2.views import get_schema_view
from rest_framework import permissions

from sales.router import router

env = environ.Env()
environ.Env.read_env()

open_api_obj = openapi.Info(
    title="Sales API",
    default_version="v1",
    description="Rest API para o desafio da Bycoders",
    terms_of_service="https://www.google.com/policies/terms/",
    contact=openapi.Contact(email="marcuspnascimento@gmail.com"),
    license=openapi.License(name="BSD License"),
)
schema_view = get_schema_view(
    open_api_obj,
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("api/", include(router.urls)),
    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'
    ),
    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    path(
        'redoc/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    ),
]
