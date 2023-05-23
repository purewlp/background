import json

from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from user.models import User
from information.models import Comment,Follow,Favorite
from video.models import Video
from information.models import Message
app_name = 'user'

@csrf_exempt
def register(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            try:
                user = User.objects.get(username=username)
                return JsonResponse({'message': "用户已存在"}, status=401)
            except User.DoesNotExist:
                newUser = User(username=username, password=password, createdTime=timezone.now())
                newUser.save()
                return JsonResponse({'msg': "注册成功"}, status=200)
    except Exception as e:
        return JsonResponse({'msg': "未知错误"}, status=402)



@csrf_exempt
def login(request):
    try:
        if request.method == 'GET':
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')

            try:
                user = User.objects.get(username=username)
                if password != user.password:
                    return JsonResponse({'msg': '密码错误'}, status=402)

                userData = {
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
                    'sign': user.sign
                }

                return JsonResponse({'message': '登录成功', 'userData': userData}, status=200)
            except User.DoesNotExist:
                return JsonResponse({'msg': '用户不存在'}, status=401)
    except Exception as e:
        return JsonResponse({'msg': '未知错误'}, status=402)


@csrf_exempt  # 跨域设置
def getlike(request):
    try:
        if request.method == 'GET':
            data = json.loads(request.body)
            id = data.get('id')
            user = User.objects.get(id=id)
            likes = Favorite.objects.filter(userId=id).values_list('videoID', flat=True)
            videos = Video.objects.filter(id__in=likes)
            videoDetails = []
            for video in videos:
                # 根据视频详情信息表的具体字段调整下面的代码
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
            return JsonResponse({'videoDetails': videoDetails, 'message': '成功返回'}, status=200,safe=False)
    except User.DoesNotExist:
        return JsonResponse({'message': '用户不存在'}, status=401)
    except Exception as e:
        return JsonResponse({'message': '未知错误'}, status=401)

@csrf_exempt
def getfollow(request):
    try:
        if request.method == 'GET':
            data = json.loads(request.body)
            userId = data.get('id')
            user = User.objects.get(id=userId)
            followings = user.following.all()
            followingsDetails = []
            for following in followings:
                followingUser = User.objects.get(id=following.followingId)
                followingsDetails.append({
                    'username': followingUser.username,
                    'avatarUrl': followingUser.avatarUrl
                })
            return JsonResponse({'followings': followingsDetails, 'message': '成功返回'}, status=200)
    except User.DoesNotExist:
        return JsonResponse({'message': '用户不存在'}, status=401)
    except Exception as e:
        return JsonResponse({'message': '未知错误'}, status=401)

#视频评论信息表中的createtime和content
@csrf_exempt
def getwords(request):
    try:
        if(request.method == 'GET'):
            data = json.loads(request.body)
            id = data.get('id')
            user= User.objects.get(id=id)
            comments = user.comment.all()
            commentsDetails = []
            for comment in comments:
                commentsDetails.append({
                    'id' : comment.id,
                    'userId': comment.userId,
                    'content' :comment.content,
                    'createdTime': comment.createdTime
                })
            return JsonResponse({'commentsDetails':commentsDetails,'message':'成功返回'}, status=200,safe=False)
    except User.DoesNotExist:
        return JsonResponse({'message': '用户不存在'}, status=401)
    except Exception as e:
        return JsonResponse({'message': '未知错误'}, status=401)

@csrf_exempt
def getmessage(request):
    try:
        if(request.method == 'GET'):
            data = json.loads(request.body)
            id = data.get('id')
            user=User.objects.get(id=id)
            messages = user.message.all()
            messagesDetails = []
            for message in messages:
                messagesDetails.append({
                    'id': message.id,
                    'title': message.title,
                    'content': message.content,
                    'createdTime': message.createdTime,
                    'isRead': message.isRead,
                    'fromName' : message.fromName
                })
            return JsonResponse({'messagesDetails':messagesDetails,'message':'成功返回'}, status=200,safe=False)
    except User.DoesNotExist:
        return JsonResponse({'message': '用户不存在'}, status=401)
    except Exception as e:
        return JsonResponse({'message': '未知错误'}, status=401)

@csrf_exempt
def avatar(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            userId = data.get('id')
            avatarFile = request.FILES.get('avatar')
            user = User.objects.get(id=userId)
            user.avatar.save(avatarFile.name, avatarFile, save=True)
            user.avatarUrl = user.avatar.url
            user.save()
            return JsonResponse({'message':'成功返回'}, status=200)
        except Exception as e:
            return JsonResponse({'message': '未知错误'}, status=401)
    else:
        return JsonResponse({'message': '未知错误'}, status=401)

@csrf_exempt
def sign(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_id = data.get('id')
            signature = data.get('sign')
            user = User.objects.get(id=user_id)
            user.sign = signature
            user.save()
            return JsonResponse({'message': '个性签名更新成功'}, status=200)
        except User.DoesNotExist:
            return JsonResponse({'message': '用户不存在'}, status=401)
        except Exception as e:
            return JsonResponse({'message': '未知错误'}, status=401)
    else:
        return JsonResponse({'message': '请求方法不允许'}, status=401)
@csrf_exempt
def deleteComment(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            commentId = data.get('id')
            comment = Comment.objects.get(id=commentId)
            comment.delete()
            return JsonResponse({'message': '评论删除成功'}, status=200)
        except Comment.DoesNotExist:
            return JsonResponse({'message': '评论不存在'}, status=401)
        except Exception as e:
            return JsonResponse({'message': '未知错误'}, status=401)
    else:
        return JsonResponse({'message': '请求方法不允许'}, status=401)

@csrf_exempt
def getVideo(request):
    if request.method == 'GET':
        data = json.loads(request.body)
        userId = data.get('id')
        try:
            videos = Video.objects.filter(userID=userId)
            if(videos.exists()):
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
                return JsonResponse({'message': '无相关视频'}, status=401)
        except Exception as e:
            return JsonResponse({'message': '未知错误'}, status=401)
    else:
        return JsonResponse({'message': '请求方法不允许'}, status=401)

@csrf_exempt
def userprofile(request):
    try:
        if request.method == 'GET':
            data = json.loads(request.body)
            id = data.get('id')
            try:
                user = User.objects.get(id=id)
                userData = {
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
                    'sign': user.sign
                }
                return JsonResponse({'message': '成功返回', 'userData': userData}, status=200,safe=False)
            except User.DoesNotExist:
                return JsonResponse({'msg': '用户不存在'}, status=401)
    except Exception as e:
        return JsonResponse({'msg': '未知错误'}, status=402)