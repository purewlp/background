from django.urls import path

from video import views

app_name = 'video'

urlpatterns = [
    path('upload/', views.upload),
    path('content/', views.content),
    path('delete/', views.delete),
]
