from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect  # 重导向
from .models import Virus
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import File
import os
import time


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
    if request.user.is_authenticated:
        if request.method == "POST":
            upload_file = request.FILES.get('file')
            if upload_file:
                media = "./media"
                alia = time.strftime("%Y_%m_%d_%H_%M_%S_", time.localtime()) + upload_file.name  # 别名保存文件
                file_path = os.path.join(os.path.join(media, 'files'), alia)
                file = File(user=request.user.username, fileName=upload_file.name, alia=alia, path=file_path)
                f = open(file_path, "wb+")
                for part in upload_file.chunks():
                    f.write(part)
                f.close()
                file.save()
                # message = {"tags": "success", "message":"Upload successfully"}
                return redirect('.', locals())
            else:
                message = {"tags":"warning", "message":"Please choose a file first"}
        return render(request, 'upload.html', locals())
    else:
        return redirect('/')


@login_required
def download(request):
    files = File.objects.filter(user=request.user.username)
    return render(request, 'download.html', locals())


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
