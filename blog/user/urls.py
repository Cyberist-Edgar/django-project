from django.urls import path
from user import views

urlpatterns = [
    path('login/', views.login),
    path('loginout/', views.loginout),
    path('signup/', views.signup),
    path('forget/',views.forget_password),
    path('change/', views.change_password),
    path('email/', views.send_email),
    path('profile/', views.profile),
    ]