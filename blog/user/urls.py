from django.urls import path
from user import views
app_name = "user"
urlpatterns = [
    path('login/', views.login, name='login'),
    path('loginout/', views.loginout, name='loginout'),
    path('signup/', views.signup, name='signup'),
    path('forget/',views.forget_password, name="forget"),
    path('change/', views.change_password, name='change'),
    path('email/', views.send_email, name='email'),
    path('profile/', views.profile, name='profile'),
    ]