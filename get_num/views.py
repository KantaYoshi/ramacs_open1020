from django.shortcuts import render
import django_filters
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Log

# Create your views here.

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Log
        fields ='__all__'

class LogFilter(django_filters.FilterSet):
    class Meta:
        model=Log
        fields={'created_at':['gte', ], }

class LogViewSet(viewsets.ModelViewSet):
    queryset=Log.objects.all().order_by("created_at")

    serializer_class=LogSerializer
    filter_class=LogFilter

    authentication_classes=(SessionAuthentication,BasicAuthentication)
    permission_classes=(IsAuthenticated,)

class MainView(LoginRequiredMixin,TemplateView):
    template_name='index.html'

# class UserPageView(LoginRequiredMixin,TemplateView):
#     template_name='user-page.html'
#     # pk取得の動作を追加して辞書形式にしてuser-page.htmlにとばす。

#class UserPageView(LoginRequiredMixin):
    #template_name='user-page.html'
def userPage(request,pk):
    return render(request,'user-page.html',{"user":request.user})

class LogOutView(TemplateView):
    template_name='logout.html'
