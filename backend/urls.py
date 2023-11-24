from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
    path('auth_api/', include('auth_api.urls')),
    path('item_management/', include('item_management.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
