"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from myapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('virus/<int:num>/', views.virus),
    path("", views.index),
    path('virus/<str:ename>/', views.virus_detail),
    path('sjtu/', views.sjtu, name='sjtu'),
    path('user/', include('user.urls')),
    path("upload/", views.upload, name='upload'),
    path("download/", views.download, name='download'),
    path("ajax/", views.ajax, name='ajax'),
    path('data/', views.data, name='data'),
    path('search/', views.search, name='search'),
    path('api/', include("api.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


