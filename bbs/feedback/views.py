from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from user.models import User

from .models import Feedback


@login_required
def index(request):
    """反馈界面"""
    if request.method == "POST":
        subject = request.POST.get("subject")
        content = request.POST.get("content")
        type = bool(int(request.POST.get("type")))
        message = None
        if not subject.strip():
            message = {"info": '主题为空', 'tag': "warning"}
        if not content.strip():
            message = {"info": "内容为空", 'tag': "warning"}
        if content.strip() and subject.strip():
            message = {"info": "反馈成功, 请等待管理员处理", "tag": "success"}
            feedback = Feedback(user_id=User.objects.get(user_id=request.user.id).id,
                                username=request.user.username,
                                subject=subject,
                                content=content,
                                type=type)
            feedback.save()
        request.session["message"] = message
        print(message)
        return redirect(reverse("feedback:index"))
    if "message" in request.session.keys():
        message = request.session.pop("message")
    else:
        message = None
    return render(request, "feedback/index.html", context={"message": message})
