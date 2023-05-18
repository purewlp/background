from django.db import models
from user.models import User
class Message(models.Model):
    title = models.CharField(max_length= 64)
    content = models.TextField()
    createdTime = models.DateTimeField(auto_now_add=True)
    userId = models.ForeignKey(User,related_name='message',on_delete=models.CASCADE)
    isRead = models.BooleanField(default= False)
    fromName = models.CharField(default='短视频平台')