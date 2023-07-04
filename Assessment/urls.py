from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dj-admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('', include('app.urls')),
    path('admin/', include('myadmin.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
