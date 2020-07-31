from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('videos.urls')),
    path('admin/', admin.site.urls),
]

# In development, this gives the dev the ability to see the url to uploaded files.
# We upload files for category pages and projects.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)