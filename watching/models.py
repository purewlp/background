from django.db import models

from information.models import Comment
from user.models import User
from video.models import Video


# Create your models here.
class Like(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    videoID = models.ForeignKey(Video, on_delete=models.CASCADE)


class LikeComment(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    commentID = models.ForeignKey(Comment, on_delete=models.CASCADE)


class Complain(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=100)
    userID = models.ForeignKey(User, related_name='complaint', on_delete=models.CASCADE)
    videoID = models.ForeignKey(Video, on_delete=models.CASCADE)
