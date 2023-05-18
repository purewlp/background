from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('login/', views.login),
    path('register/', views.register),
    path('getlike/',views.getlike),
    path('getfollow/',views.getfollow),
    path('getwords/',views.getwords),
    path('getmessage/',views.getmessage),
]