from django.http import HttpResponse
from django.shortcuts import render
from post.models import Post, PostComment, PostReply
from user.models import User


def index(request):
    """社区首页"""
    posts = Post.objects.all()
    return render(request, 'community/index.html', context={"posts": posts})


def detail(request, id):
    """帖子详情"""
    post = Post.objects.get(id=id)  # 获取对应的帖子，为 Post 数据库模型
    if post:
        reply = PostReply.objects.filter(post_id=id)  # 主回复内容  为PostReply 数据库模型  中间包含对于该帖子所有的第一层上的回复信息
        data = []
        for i in reply:
            data.append({"user": User.objects.get(user_id=i.post_user_id), "reply": i, "comments": PostComment.objects.filter(post_id=id, detail_id=i.id).order_by("date")})

        return render(request, 'community/detail.html',
                      context={"post": post, "data": data, "total": reply.count()})
    else:
        return HttpResponse("404")
