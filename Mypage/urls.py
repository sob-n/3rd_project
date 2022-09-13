from django.shortcuts import render
from django.urls import path
from django.contrib.auth import views as auth_views

from Mypage import views

app_name = 'Mypage'

urlpatterns = [
    path('mypage/', views.mypage, name='mypage'),
    path('profile/', views.profile, name='profile'),
]