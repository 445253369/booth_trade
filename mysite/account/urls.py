from django.urls import path
from account import views


app_name='account'

urlpatterns = [
    path('login/',views.Login,name='login'),
    path('register/',views.register,name='register'),
    path('center/',views.center,name='center'),
    path('renewal/<int:booth_id>',views.renewal,name='renewal'),
    path('unsubscribe/<int:booth_id>',views.unsubscribe,name='unsubscribe'),
    path('pwdoperate/',views.change_password,name='pwdoperate'),
    path('logout/',views.logout,name='logout')
    # path('center/',views.UserCenter),
]