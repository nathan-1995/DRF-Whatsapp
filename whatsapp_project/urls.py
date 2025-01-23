from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from whatsapp_integration import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.redirect_to_swagger),  # This will redirect to Swagger UI
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),  # OpenAPI schema generation
    path('api/docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),  # Swagger UI
    path('api/docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),  # ReDoc UI
    path('api/', include('whatsapp_integration.urls')),  # Include app URLs under `/api/`

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # Serve static files in development mode