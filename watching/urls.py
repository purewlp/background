from django.urls import path

from watching import views

app_name = 'watching'

urlpatterns = [
    path('like/', views.like),
    path('save/', views.save),
    path('dislike/', views.dislike),
    path('dissave/', views.dissave),
    path('likecomment/', views.likecomment),
    path('dislikecomment/', views.dislikecomment),
    path('pass/', views.passvideo),
    path('message/', views.message),
    path('complain', views.complain),
    path('getvideo/', views.getvideo)
]
