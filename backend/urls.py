from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth_api/', include('auth_api.urls')),
    path('api/item_management/', include('item_management.urls')),
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
