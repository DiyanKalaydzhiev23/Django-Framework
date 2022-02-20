from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from templates_advanced import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pythons_app.urls')),
    path('auth/', include('pythons_auth.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
