from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect  # 重导向
from .models import Virus
from django.contrib.sessions.models import Session
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.conf import settings
from django.core.paginator import Paginator
from django.http import JsonResponse


# Create your views here.
def index(request):
    """主页面"""
    # try:
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None

    return render(request, 'index.html', locals())
    # except:
    #     return redirect("/")


def virus(request, num):
    """省份疫情页面"""
    try:
        virus = Virus.objects.all().order_by("name")
        paginator = Paginator(virus, 10)

        virus = paginator.page(num)  # 每一次返回的数据

        return render(request, 'virus.html', locals())
    except:
        return redirect("/")


def virus_detail(request, ename):
    """省份页面详情"""
    try:
        detail = Virus.objects.get(ename=ename)
        if detail:
            return render(request, 'detail.html', context={"detail": detail})
    except:
        return redirect("/")


def sjtu(request):
    return render(request, 'sjtu.html')


def upload(request):
    if request.method == "POST":
        upload_file = request.FILES.get('file')
        if upload_file:
            f = open(upload_file.name, "wb+")
            for part in upload_file.chunks():
                f.write(part)
            f.close()
        else:
            messages.add_message(request, messages.WARNING, "Please choose a file first")
    return render(request, 'upload.html', locals())


def download(request):
    return render(request, 'download.html')


def page(request):
    virus = Virus.objects.all().order_by("name")
    p = Paginator(virus, 10)  # 10 个为一页


def data(request):
    virus = Virus.objects.values()
    data = []
    for i in virus:
        data.append(i)
    # data = [i for i in virus]
    return JsonResponse({"data": data})


def ajax(request):
    return render(request, 'ajax.html')
