from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from user import views

app_name = 'user'



urlpatterns = [
    path('login/', views.login),
    path('register/', views.register),
    path('getlike/',views.getlike),
    path('getfollow/',views.getfollow),
    path('getwords/',views.getwords),
    path('getmessage/',views.getmessage),
    path('avatar/',views.avatar),
    path('sign/',views.sign),
    path('deletecontent/',views.deletecontent),
    path('getvideo/',views.getVideo),
    path('userprofile/',views.userprofile),
    path('follow/',views.follow),
    path('disfollow/',views.disfollow),
    path('getcomplain/',views.getcomplain),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)