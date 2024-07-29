from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Hotel Room Rate Management API",
      default_version='v1',
      description="API documentation for managing hotel room rates",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@hotel.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('admin/', admin.site.urls),
        path('api/', include('room_rates.urls')),
]
