from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    videoNum = models.IntegerField(default=0)
    likeNum = models.IntegerField(default=0)
    collectNum = models.IntegerField(default=0)
    fanNum = models.IntegerField(default=0)
    followNum = models.IntegerField(default=0)
    avatar = models.FileField(upload_to='avatar/')
    createdTime = models.TimeField()
