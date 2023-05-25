import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from information.models import Favorite, Message, Comment
from user.models import User
from video.models import Video
from watching.models import Like, Complain, LikeComment


# Create your views here.
@csrf_exempt
def like(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            id = data.get('id')
            userID = data.get('userID')
            videoID = data.get('videoID')
            newLike = Like(id=id, userID=userID, videoID=videoID)
            newLike.save()
            likeNum_video = Video.objects.get(id=videoID).likeNum
            likeNum_user = User.objects.get(id=Video.objects.get(id=videoID).userID).likeNum
            bl_video = Video.objects.filter(id=videoID).update(likeNum=likeNum_video + 1)
            bl_user = User.objects.filter(id=Video.objects.get(id=videoID).userID).update(likeNum=likeNum_user + 1)
            if bl_video == 1 and bl_user == 1:
                return JsonResponse({'msg': "点赞成功"}, status=200)
            else:
                return JsonResponse({'msg': "未知错误"}, status=401)
    except Exception as e:
        return JsonResponse({'msg': "未知错误"}, status=401)


@csrf_exempt
def save(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            id = data.get('id')
            userID = data.get('userID')
            videoID = data.get('videoID')
            newFavorite = Favorite(id=id, userID=userID, videoID=videoID)
            newFavorite.save()
            collectNum_video = Video.objects.get(id=videoID).collectNum
            collectNum_user = User.objects.get(id=Video.objects.get(id=videoID).userID).collectNum
            bl_video = Video.objects.filter(id=videoID).update(collectNum=collectNum_video + 1)
            bl_user = User.objects.filter(id=Video.objects.get(id=videoID).userID).update(
                collectNum=collectNum_user + 1)
            if bl_video == 1 and bl_user == 1:
                return JsonResponse({'msg': "点赞成功"}, status=200)
            else:
                return JsonResponse({'msg': "未知错误"}, status=401)
    except Exception as e:
        return JsonResponse({'msg': "未知错误"}, status=401)


@csrf_exempt
def dislike(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            id = data.get('id')
            userID = data.get('userID')
            videoID = data.get('videoID')
            likeNum_video = Video.objects.get(id=videoID).likeNum
            likeNum_user = User.objects.get(id=Video.objects.get(id=videoID).userID).likeNum
            bl_video = Video.objects.filter(id=videoID).update(likeNum=likeNum_video - 1)
            bl_user = User.objects.filter(id=Video.objects.get(id=videoID).userID).update(likeNum=likeNum_user - 1)
            Like.objects.get(id=id).delete()
            if bl_video == 1 and bl_user == 1:
                return JsonResponse({'msg': "点赞成功"}, status=200)
            else:
                return JsonResponse({'msg': "未知错误"}, status=401)
    except Exception as e:
        return JsonResponse({'msg': "未知错误"}, status=401)


@csrf_exempt
def dissave(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            id = data.get('id')
            userID = data.get('userID')
            videoID = data.get('videoID')
            collectNum_video = Video.objects.get(id=videoID).collectNum
            collectNum_user = User.objects.get(id=Video.objects.get(id=videoID).userID).collectNum
            bl_video = Video.objects.filter(id=videoID).update(collectNum=collectNum_video - 1)
            bl_user = User.objects.filter(id=Video.objects.get(id=videoID).userID).update(
                collectNum=collectNum_user - 1)
            Favorite.objects.get(id=id).delete()
            if bl_video == 1 and bl_user == 1:
                return JsonResponse({'msg': "点赞成功"}, status=200)
            else:
                return JsonResponse({'msg': "未知错误"}, status=401)
    except Exception as e:
        return JsonResponse({'msg': "未知错误"}, status=401)


@csrf_exempt
def likecomment(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            id = data.get('id')
            userID = data.get('userID')
            newlike = LikeComment(userID=userID, commentID=id)
            newlike.save()

            return JsonResponse({'msg': "点赞成功"}, status=200)
    except Exception as e:
        return JsonResponse({'msg': "未知错误"}, status=401)


@csrf_exempt
def dislikecomment(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            id = data.get('id')
            userID = data.get('userID')
            LikeComment.objects.get(userID=userID, commentID=id).delete()

            return JsonResponse({'msg': "取消点赞成功"}, status=200)
    except Exception as e:
        return JsonResponse({'msg': "未知错误"}, status=401)


@csrf_exempt
def passvideo(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            videoID = data.get('videoID')
            Video.objects.get(id=videoID).update(needAudit=0)
            Complain.objects.filter(videoID=videoID).delete()
            return JsonResponse({'msg': "通过成功"}, status=200)

    except Exception as e:
        return JsonResponse({'msg': "未知错误"}, status=401)


@csrf_exempt
def message(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            title = data.get('title')
            content = data.get('content')
            createdTime = data.get('createdTime')
            userID = data.get('userID')
            fromName = data.get('fromName')
            newMessage = Message(title=title, content=content, createdTime=createdTime, userID=userID, fromName=fromName)
            newMessage.save()
            return  JsonResponse({'msg': "发送成功"}, status=200)

    except Exception as e:
        return JsonResponse({'msg': "未知错误"}, status=401)


@csrf_exempt
def complain(request):
    try:
        if request == 'POST':
            data = json.loads(request.body)
            id = data.get('id')
            description = data.get('description')
            userID = data.get('userID')
            videoID = data.get('videoID')
            newComplain = Complain(id=id, description=description, userID=userID, videoID=videoID)
            newComplain.save()
            Video.objects.get(videoID=videoID).update(needAudit=1)
            return JsonResponse({'msg': "投诉成功"}, status=200)

    except Exception as e:
        return JsonResponse({'msg': "未知错误"}, status=401)

@csrf_exempt
def getvideo(request):
    try:
        if request.method == 'GET':
            data = json.loads(request.body)
            videoID = data.get('videoID')
            userID = data.get('userID')
            video = Video.objects.get(id=videoID)
            user = User.objects.get(id=userID)
            video.update(viewNum=video.viewNum+1)
            comments = Comment.objects.filter(videoID=videoID)
            commentList = []
            if comments.exists():
                for comment in comments:
                    commentList.append({
                        'id': comment.id,
                        'userID': comment.userId,
                        'avatarUrl': User.objects.get(id=comment.userId).avatarUrl,
                        'username': User.objects.get(id=comment.userId).username,
                        'content': comment.content,
                        'isLike': LikeComment.objects.filter(userID=userID, commentID=comment.id).exists(),
                        'likeNum': LikeComment.objects.filter(commentID=comment.id).count(),
                        'isOwn': comment.userId == userID
                    })
            return JsonResponse(
                {
                    'msg': "观看成功",
                    'avatarUrl': user.avatarUrl,
                    'collectNum': video.collectNum,
                    'description': video.description,
                    'videoID': videoID,
                    'needAudit': video.needAudit,
                    'likeNum': video.likeNum,
                    'title': video.title,
                    'userID': userID,
                    'videoUrl': video.videoUrl,
                    'zone': video.zone,
                    'isLiked': Like.objects.filter(userID=userID, videoID=videoID).exists(),
                    'isCollectted': Favorite.objects.filter(userID=userID, videoID=videoID).exists(),
                    'commentNum': Comment.objects.filter(videoID=videoID).count(),
                    'commentList': commentList,
                    'user': User.objects.get(id=Video.objects.get(id=videoID).userID),
                    'createdTime': video.createdTime,
                    'viewNum': video.viewNum
                 },
                status=200
            )

    except Exception as e:
        return JsonResponse({'msg': "视频不存在"}, status=401)
