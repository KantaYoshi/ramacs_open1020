"""change_slack URL Configuration

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
from django.urls import path,include
from rest_framework import routers

from get_num.views import LogViewSet
from get_num.views import MainView,LogOutView,userPage,KanriView

router =routers.DefaultRouter()
router.register(r'logs',LogViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('',MainView.as_view(),name="index"),#indexページに変更,index.htmlはユーザーページにする。
    path('logout/',LogOutView.as_view(),name="logout"),
    path('user-page/<int:pk>/',userPage,name="user-page"),
    # path('kanri-page/',KanriView.workKanriView,name="kanri-page"),
    path('kanri-page/',KanriView.as_view(),name="kanri-page"),
    path('/admin/password_change/',admin.site.urls),
    # path('tamago/',include('get_num.urls')),
]

admin.site.site_header='RAMACS (Remote-Work Attendance Management And Communication Support)'
