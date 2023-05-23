from django.db import models
from user.models import User
from video.models import Video


class Message(models.Model):
    title = models.CharField(max_length= 64)
    content = models.TextField()
    createdTime = models.DateTimeField(auto_now_add=True)
    userId = models.ForeignKey(User,related_name='message',on_delete=models.CASCADE)
    isRead = models.BooleanField(default= False)
    fromName = models.CharField(max_length=1024,default='短视频平台')


class Favorite(models.Model):
    userId = models.ForeignKey(User,on_delete=models.CASCADE)
    videoID = models.ForeignKey(Video,on_delete=models.CASCADE)

class Follow(models.Model):
    followerId = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE) #关注者
    followingId = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE) #被关注者

class Comment(models.Model):
    userId = models.ForeignKey(User,related_name='comment',on_delete=models.CASCADE)
    createdTime = models.DateTimeField(auto_now_add=True)
    updatedTime = models.DateTimeField(auto_now= True)
    content = models.TextField()
    videoId = models.ForeignKey(Video,related_name='comment',on_delete=models.CASCADE)