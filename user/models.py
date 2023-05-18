from django.contrib.auth.models import AbstractUser
from django.db import models
from video.models import Video
from information.models import Message
class User(AbstractUser):
    videoNum = models.IntegerField(default=0)
    likeNum = models.IntegerField(default=0)
    collectNum = models.IntegerField(default=0)
    fanNum = models.IntegerField(default=0)
    followNum = models.IntegerField(default=0)
    avatar = models.FileField(upload_to='avatar/')
    createdTime = models.DateTimeField(auto_now_add= True)

class Favorite(models.Model):
    userId = models.ForeignKey(User,on_delete=models.CASCADE)
    videoID = models.ForeignKey(Video,on_delete=models.CASCADE)

class Follow(models.Model):
    followerId = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE) #关注者
    followingId = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE) #被关注者
