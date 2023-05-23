import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from video.models import Video
from user.models import User
from information.models import Follow
@csrf_exempt
def video(request):
    if request.method == 'GET':
        try:
            data = json.loads(request.body)
            search_str = data.get('search_str')
            videos = Video.objects.filter(title__icontains=search_str)
            if videos.exists():
                videoDetails = []
                for video in videos:
                    videoDetails.append({
                        'title': video.title,
                        'description': video.description,
                        'coverUrl': video.coverUrl,
                        'videoUrl': video.videoUrl,
                        'avatarUrl': video.avatarUrl,
                        'likeNum': video.likeNum,
                        'collectNum': video.collectNum,
                        'viewNum': video.viewNum,
                        'zone': video.zone,
                        'tag': video.tag,
                        'userID': video.userID,
                        'createdTime': video.createdTime,
                        'needAudit': video.needAudit,
                    })
                return JsonResponse({'videos': videoDetails}, status=200,safe=False)
            else:
                return JsonResponse({'message': '视频不存在'}, status=401)
        except Exception as e:
            return JsonResponse({'message': '未知错误'}, status=401)
    else:
        return JsonResponse({'message': '请求方法不允许'}, status=401)

@csrf_exempt
def user(request):
    if request.method == 'GET':
        data = json.loads(request.body)
        search_str = data.get('search_str')
        users = User.objects.filter(username__icontains=search_str)
        if users.exists():
            userInfo = []
            for user in users:
                userInfo.append({
                    'id': user.id,
                    'username': user.username,
                    'password': user.password,
                    'videoNum': user.videoNum,
                    'likeNum': user.likeNum,
                    'collectNum': user.collectNum,
                    'fanNum': user.fanNum,
                    'followNum': user.followNum,
                    'avatarUrl': user.avatarUrl,
                    'isSuperAdmin': user.isSuperAdmin,
                    'createdTime': user.createdTime,
                    'sign' : user.sign
                })
            return JsonResponse({'users': userInfo}, status=200)
        else:
            return JsonResponse({'message': '用户不存在'}, status=401)
    else:
        return JsonResponse({'message': '请求方法不允许'}, status=401)

@csrf_exempt
def zone(request):
    if request.method == 'GET':
        data = json.loads(request.body)
        zone = data.get('zone')
        if zone:
            videos = Video.objects.filter(zone=zone).order_by('viewNum', 'likeNum')
        else:
            videos = Video.objects.all().order_by('viewNum', 'likeNum')
        if videos.exists():
            videoDetails = []
            for video in videos:
                videoDetails.append({
                    'id':video.id,
                    'title' : video.title,
                    'description' : video.description,
                    'coverUrl' : video.coverUrl,
                    'videoUrl' : video.videoUrl,
                    'avatarUrl' : video.avatarUrl,
                    'likeNum' : video.likeNum,
                    'collectNum' : video.collectNum,
                    'viewNum' :video.viewNum,
                    'zone' : video.zone,
                    'tag' : video.tag,
                    'userID' : video.userID,
                    'createdTime' : video.createdTime,
                    'needAudit' : video.needAudit

                })
            return JsonResponse({'videos': videoDetails}, status=200,safe=False)
        else:
            return JsonResponse({'message': '视频不存在'}, status=401)
    else:
        return JsonResponse({'message': '请求方法不允许'}, status=401)

@csrf_exempt
def getfollow(request):
    if request.method == 'GET':
        data = json.loads(request.body)
        userId = data.get('id')
        try:
            user = User.objects.get(id = userId)
        except User.DoesNotExist:
            return JsonResponse({'message': '用户不存在'}, status=401)
        try:
            followings = Follow.objects.filter(followerId=userId)
            videos = Video.objects.filter(userId__in=[following.followingId for following in followings])
            video_list = []
            for video in videos:
                video_list.append({
                    'id':video.id,
                    'title' : video.title,
                    'description' : video.description,
                    'coverUrl' : video.coverUrl,
                    'videoUrl' : video.videoUrl,
                    'avatarUrl' : video.avatarUrl,
                    'likeNum' : video.likeNum,
                    'collectNum' : video.collectNum,
                    'viewNum' :video.viewNum,
                    'zone' : video.zone,
                    'tag' : video.tag,
                    'userId' : video.userId,
                    'createdTime' : video.createdTime,
                    'needAudit' : video.needAudit
                    })

            return JsonResponse({'videos': video_list, 'message': '成功返回'}, status=200,safe=False)
        except Exception as e:
            return JsonResponse({'message': '未知错误'}, status=401)
    else:
        return JsonResponse({'message': '请求方法不允许'}, status=401)