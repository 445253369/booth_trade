from django.urls import path
from .views import *

app_name = 'account'
urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', logout, name="logout"),  # 注销登录
    path('register/', register, name='register'),  # 注册
    path('center/', center, name='center'),
    path('change_profile/', change_profile, name='change_profile'), # 修改资料
]