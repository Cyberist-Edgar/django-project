from django.conf import settings
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.http import Http404
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives


# Create your views here.


def login(request):
    """登录页面"""
    try:
        if request.method == 'POST':
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    messages.add_message(request, messages.SUCCESS, 'login in successfully')
                    return redirect('/')
                else:
                    messages.add_message(request, messages.WARNING, '账号被冻结')
            else:
                messages.add_message(request, messages.INFO, '无此账号')

        return render(request, 'login.html')

    except Exception as e:
        raise Http404("error")


@login_required()
def loginout(request):
    auth.logout(request)
    return redirect('/')
    # if request.method == 'GET':
    #     Session.objects.all().delete()
    #     # request.session['username'] = None
    # else:
    #     return Http404('')
    # return redirect('/')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm")
        user_flag = User.objects.filter(username=username)

        if user_flag:
            messages.add_message(request, messages.WARNING, '该用户已经创建')
        else:
            if password == confirm:
                user = User.objects.create_user(username=username, password=password)  # 创建一个新的用户
                user.save()
                messages.add_message(request, messages.SUCCESS, "创建成功")
                return redirect(".")
            else:
                messages.add_message(request, messages.INFO, "两次输入的密码不对")

    return render(request, 'signup.html', locals())


def forget_password(request):
    pass


@login_required(login_url="/user/login")
def change_password(request):
    if request.method == 'POST':
        username = request.POST.get('old_password')
        password = request.POST.get('new_password1')
        confirm = request.POST.get('new_password2')
        if username and password and confirm:
            user = User.objects.filter(username=username).all()
            print(user)
            if user.exists():
                user = user[0]
                print(user.password)
                if user.check_password(password):
                    if password == confirm:
                        message = {"data": "修改成功", "tags": "success"}
                        request.user.set_password(password)
                        loginout(request)
                        return redirect("/user/login")
                    else:
                        message = {"data": "两次密码不正确", "tags": "warning"}
                else:
                    message = {"data": "密码不正确", "tags": "warning"}
            else:
                message = {"data": "不存在该用户", "tags": "warning"}
        else:
            message = {"data": "请填写每一空", "tags": "warning"}
        return render(request, 'change.html', locals())
    else:
        return render(request, "change.html")


@login_required(login_url="/user/login")
def send_email(request):
    if request.method == 'POST':
        to = request.POST.get('email')
        subject = request.POST.get('subject')
        content = request.POST.get('content')
        file = request.FILES.get("file")
        try:
            msg = EmailMultiAlternatives(subject, content, from_email=settings.DEFAULT_FROM_EMAIL
                                         , to=[to])
            msg.attach(file.name, file.read())
            msg.send()
            # send_mail(subject, content, from_email=settings.DEFAULT_FROM_EMAIL,
            #           recipient_list=[to])
            message = {"data": "发送成功", "tags": "success"}
            return redirect('.')
        except Exception as e:
            print(e)
            message = {"data": "邮件发送失败", "tags": "warning"}
        return render(request, 'email.html', locals())
    else:
        return render(request, 'email.html', locals())


def profile(request):
    """用户的个人信息页"""
    if request.user.is_authenticated:
        user = request.user
        return render(request, 'profile.html', locals())
    else:
        return redirect('/user/login')
