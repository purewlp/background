from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
  #  path('api/video/', include(('video.urls', 'video'))),
    path('user/', include('user.urls')),
    path('index/', include('index.urls')),
    path('video/', include('video.urls')),
    path('video/', include('watching.urls'))
]


