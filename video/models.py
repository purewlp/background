from django.db import models
from user.models import User
class Video(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    coverUrl = models.CharField(max_length=64)
    videoUrl = models.CharField(max_length=64)
    avatarUrl = models.CharField(max_length=64)
    likeNum = models.IntegerField(default=0)
    collectNum = models.IntegerField(default=0)
    viewNum = models.IntegerField(default=0)
    zone = models.CharField(max_length=64)
    tag = models.CharField(max_length=64)
    userID = models.ForeignKey(User,related_name='videos',on_delete=models.CASCADE)
    createdTime = models.DateField()
    needAudit = models.IntegerField(default=0)

class Comment(models.Model):
    userId = models.ForeignKey(User,related_name='comment',on_delete=models.CASCADE)
    createdTime = models.DateTimeField(auto_now_add=True)
    updatedTime = models.DateTimeField(auto_now= True)
    content = models.TextField()
    videoId = models.ForeignKey(Video,related_name='comment',on_delete=models.CASCADE)
