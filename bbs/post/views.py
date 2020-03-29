from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@login_required
@csrf_exempt
def index(request):
    """发帖的界面"""
    return render(request, "post/index.html")
