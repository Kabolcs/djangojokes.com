from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import private_storage.urls

urlpatterns = [
    # Admin
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),

    # User Management
    path('account/', include('allauth.urls')),
    path('account/', include('users.urls')),

    # Local Apps
    path('jobs/', include('jobs.urls')),
    path('jokes/', include('jokes.urls')),
    path('', include('pages.urls')),
    
       # Private media
    path('media/private/', include(private_storage.urls)),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)