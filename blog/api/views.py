from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
import random


# Create your views here.
@csrf_protect
def email(request):
    if request.method == 'POST':
        to = request.POST.get("email")
        subject = request.POST.get("subject")
        rand = random.randint(300000, 999999)
        content = f"本次验证码为 {rand}  如果不是本人操作，请忽略"
        data = {"status": "success", "code": rand}
        try:
            send_mail(subject, from_email=settings.DEFAULT_FROM_EMAIL, message=content, recipient_list=[to])
        except Exception as e:
            print(e)
            data["status"] = "fail"
            data["code"] = None
        else:
            pass
        return JsonResponse(data)
    else:
        return render(request, 'email.html', locals())
