from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="toy project API",
        default_version="v1",
        description="some description",
        terms_of_service="https://www.where.com/policies/terms/",
        contact=openapi.Contact(email="someone@email"),
        license=openapi.License(name="some License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

swagger_url_patterns = [
    url(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    url(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "swagger-static/",
        TemplateView.as_view(
            template_name="swagger-ui.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="swagger-ui",
    ),
]

urlpatterns = (
    swagger_url_patterns
    + [
        path("admin/", admin.site.urls),
        path("api/users/", include("users.urls")),
        path("api/auth/", include("auth.urls")),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
