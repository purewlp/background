from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from index import views

app_name = 'index'



urlpatterns = [
    path('video/', views.video),
    path('user/',views.user),
    path('zone/',views.zone),
    path('getfollow/',views.getfollow),


]