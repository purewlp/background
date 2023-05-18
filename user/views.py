from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from .models import User,Favorite
from video.models import Video
from information.models import Message

@csrf_exempt    # 跨域设置
def register(request):  # 继承请求类
    try:
        if request.method == 'POST':
            username = request.POST.get('username')  # 获取请求体中的请求数据
            password = request.POST.get('password')
            if(User.objects.get(username= username)):
                return JsonResponse({'message': "用户已存在"},status=401)
            else:
                newUser = User(username=username, password=password,createdTime=timezone.now())
                newUser.save()
                return JsonResponse({'msg': "注册成功"},status=200)
    except Exception as e:
        return JsonResponse({'msg': "未知错误"},status=402)

@csrf_exempt  # 跨域设置
def login(request):  # 继承请求类
    try:
         if request.method == 'GET':
            username = request.GET.get('username')  # 获取请求体中的请求数据
            password = request.GET.get('password')
            user=User.objects.get(username=username)
            if(user== None):
                return JsonResponse({'msg':'用户不存在'},status=401)
            elif(password!=user.password):
                return JsonResponse({'msg':'密码错误'},status=402)
            else:
                userData = {
                    'id': user.id,
                    'username': user.username,
                    'password': user.password,
                    'videoNum': user.videoNum,
                    'likeNum': user.likeNum,
                    'collectNum': user.collectNum,
                    'fanNum': user.fanNum,
                    'followNum': user.followNum,
                    'avatar': user.avatar,
                    'isSuperAdmin': user.is_superuser,
                    'createdTime': user.createdTime
                }
                return JsonResponse({'message': '登录成功','userData' : userData}, status=200)
    except Exception as e:
        return JsonResponse({'msg': "未知错误"},status=402)

@csrf_exempt  # 跨域设置
def getlike(request):
    try:
        if request.method == 'GET':
            id = request.GET.get('id')
            likes = Favorite.objects.filter(userId=id).values_list('videoID', flat=True)
            videos = Video.objects.filter(id=likes)
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
            return JsonResponse(videoDetails,{'message':'成功返回'}, status=200)
    except Exception as e:
        return JsonResponse({'message': '未知错误'}, status=401)

@csrf_exempt
def getfollow(request):
    try:
        if(request.method== 'GET'):
            id=request.GET.get('id')
            user = User.objects.get(id=id)
            followings = user.following.all()
            followingsDetails = []
            for following in followings:
                followingUser = User.objects.get(id = following.followingId)
                followingsDetails.append([{
                    'username': followingUser.username,
                    'avatar': followingUser.avatar
                }])
            return JsonResponse(followingsDetails,{'message':'成功返回'}, status=200)
    except Exception as e:
        return JsonResponse({'message': '未知错误'}, status=401)

#视频评论信息表中的createtime和content
@csrf_exempt
def getwords(request):
    try:
        if(request.method == 'GET'):
            id = request.GET.get('id')
            user=User.objects.get(id=id)
            comments = user.comment.all()
            commentsDetails = []
            for comment in comments:
                commentsDetails.append({
                    'content' :comment.content,
                    'createdTime': comment.createdTime
                })
            return JsonResponse(commentsDetails,{'message':'成功返回'}, status=200)
    except Exception as e:
        return JsonResponse({'message': '未知错误'}, status=401)

@csrf_exempt
def getmessage(request):
    try:
        if(request.method == 'GET'):
            id = request.GET.get('id')
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
            return JsonResponse(messagesDetails,{'message':'成功返回'}, status=200)
    except Exception as e:
        return JsonResponse({'message': '未知错误'}, status=401)