
from django.db import models

class User(models.Model):
    username = models.CharField( max_length=30)
    password = models.CharField( max_length=32)
    isSuperAdmin = models.BooleanField(default=False)
    videoNum = models.IntegerField(default=0)
    likeNum = models.IntegerField(default=0)
    collectNum = models.IntegerField(default=0)
    fanNum = models.IntegerField(default=0)
    followNum = models.IntegerField(default=0)
    avatar = models.FileField(upload_to='avatar/')
    createdTime = models.DateTimeField(auto_now_add= True)
    avatarUrl =models.CharField( max_length=128, default='')
    sign = models.CharField(max_length=1024,default='')




