from django.urls import path
from .views import *

app_name = "community"
urlpatterns = [
    path("", index, name='index'),
    path("post/<int:id>", detail, name='detail'),
]
