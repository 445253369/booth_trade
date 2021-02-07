"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from mysite import settings
from booth.views import *

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:bid>', detail, name='detail'),
    url(r'^search$', search, name='search'),
    path('rent/', rent, name='rent'), # 申请
    path('unsubscribe/<int:rid>', unsubscribe, name='unsubscribe'), # 退订
    path('cancel_unsub/<int:cid>', cancel_ubsub, name='cancel_unsub'), # 取消退订
    path('delay/<int:rid>', delay, name='delay'),
    path('account/', include('account.urls'), name='account'),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL) # 配置静态资源的路径

