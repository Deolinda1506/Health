from django.contrib import admin
from django.urls import include, path
from authentication import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg.generators import OpenAPISchemaGenerator
from appointments.views import homepage  
from authentication import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static





from authentication.serializers import UserSerializer

# Custom Schema Generator
class CustomSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)

        for path, path_item in schema.paths.items():
            for method, operation_or_operations in path_item.items():
                if method.upper() in ['PUT', 'POST', 'PATCH']:
                    if not hasattr(operation_or_operations, 'parameters'):
                        operation_or_operations.parameters = []

                    operation_or_operations.parameters.append(
                        openapi.Parameter(
                            name='body',
                            in_=openapi.IN_BODY,
                            required=True,
                            schema=self.serializer_to_schema(UserSerializer),
                        )
                    )
        return schema

    def serializer_to_schema(self, serializer):
        properties = {}
        for field_name, field in serializer.fields.items():
            field_type = openapi.TYPE_STRING
            if isinstance(field, serializers.IntegerField):
                field_type = openapi.TYPE_INTEGER
            elif isinstance(field, serializers.FloatField):
                field_type = openapi.TYPE_NUMBER
            elif isinstance(field, serializers.BooleanField):
                field_type = openapi.TYPE_BOOLEAN

            properties[field_name] = openapi.Schema(type=field_type)

        return openapi.Schema(type=openapi.TYPE_OBJECT, properties=properties)


# Swagger Schema View
schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
        description="API Description",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    generator_class=CustomSchemaGenerator,
)

# URL Configuration
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login', views.MyTokenObtainPairView.as_view(), name="get_token"),
    path('api/token/refresh', TokenRefreshView.as_view(), name="refresh_token"),
    path('api/', include('authentication.urls')),
    path('api/appointments/', include('appointments.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', auth_views.home, name='home'),  # Make sure this line is present
    path('home/', views.homepage, name='healthconnect-home'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
