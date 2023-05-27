import datetime

import json
import os
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

from information.models import Comment
from short_video_backend.settings import BASE_DIR
from user.models import User
from video.models import Video


@csrf_exempt
def upload(request):  # get video and cover
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            videoID = data.get('videoID')
            title = data.get('title')
            description = data.get('description')
            zone = data.get('zone')
            userID = data.get('userID')

            dir_video = os.path.join(os.path.join(BASE_DIR, 'static'), 'videos')
            dir_cover = os.path.join(os.path.join(BASE_DIR, 'static'), 'cover')

            if not os.path.exists(dir_video):
                os.mkdir(dir_video)
            if not os.path.exists(dir_cover):
                os.mkdir(dir_cover)

            video = request.FILES.get('video')
            cover = request.FILES.get('cover')

            dir_video = os.path.join(dir_video, video.name)
            dest = open(dir_video, 'wb+')
            for chunk in video.chunks():
                dest.write(chunk)
            dest.close()
            dir_cover = os.path.join(dir_cover, cover.name)
            dest = open(dir_cover, 'wb+')
            for chunk in cover.chunks():
                dest.write(chunk)
            dest.close()

            videoUrl = dir_video
            coverUrl = dir_cover
            newVideo = Video(videoID=videoID, title=title, description=description, coverUrl=coverUrl,
                             videoUrl=videoUrl, zone=zone, userID=userID, createdTime=datetime.datetime.now())
            User.objects.get(userID=userID).update(videoNum=User.objects.get(userID=userID).videoNum+1)
            newVideo.save()
            return JsonResponse({'message': "上传成功"}, status=200)
    except Exception as e:
        return JsonResponse({'message': "未知错误"}, status=401)


@csrf_exempt
def content(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            id = data.get('id')
            username = data.get('username')
            content = data.get('content')
            videoID = data.get('videoID')
            newComment = Comment(id=id, username=username, content=content, videoID=videoID)
            newComment.save()
            return JsonResponse({'message': "上传成功"}, status=200)
    except Exception as e:
        return JsonResponse({'message': "未知错误"}, status=401)


@csrf_exempt
def delete(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            videoID = data.get('videoID')
            dir_video = Video.objects.get(id=videoID).videoUrl
            dir_cover = Video.objects.get(id=videoID).coverUrl
            os.remove(dir_video)
            os.remove(dir_cover)
            user = User.objects.get(id=Video.objects.get(id=videoID).userID)
            user.update(videoNum=user.videoNum-1)
            Video.objects.get(id=videoID).delete()

            return JsonResponse({'message': "删除成功"}, status=200)

    except Exception as e:
        return JsonResponse({'message': "未知错误"}, status=401)
