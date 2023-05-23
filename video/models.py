from django import apps
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
    userId = models.ForeignKey(User,related_name='videos',on_delete=models.CASCADE)
    createdTime = models.DateField()
    needAudit = models.IntegerField(default=0)


