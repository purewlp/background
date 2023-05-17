from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from user.models import User


@csrf_exempt    # 跨域设置
def register(request):  # 继承请求类
    if request.method == 'POST':
        username = request.POST.get('username')  # 获取请求体中的请求数据
        password = request.POST.get('password')
        if(User.objects.get(username= username)):
            return JsonResponse({'message': "用户已存在"},status=401)
        else:
            newUser = User(username=username, password=password,createdTime=timezone.now())
            newUser.save()
            return JsonResponse({'msg': "注册成功"},status=200)
    else:
        return JsonResponse({'msg': "未知错误"},status=402)

@csrf_exempt  # 跨域设置
def login(request):  # 继承请求类
     if request.method == 'get':
        username = request.GET.get('username')  # 获取请求体中的请求数据
        password = request.GET.get('password')
        user=User.objects.get(username=username)
        if(user== None):
            return JsonResponse({'msg':'用户不存在'},status=401)
        elif(password!=user.password):
            return JsonResponse({'msg':'密码错误'},status=402)
        else:
            userData = {
                'id':user.id,
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
     else:
        return JsonResponse({'msg': "未知错误"},status=402)