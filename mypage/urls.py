from django.shortcuts import render
from django.urls import path
from django.contrib.auth import views as auth_views

from mypage import views

app_name = 'mypage'

urlpatterns = [
    path('', views.mypage, name='mypage'),
    # path('profile/', views.profile, name='profile'),
]