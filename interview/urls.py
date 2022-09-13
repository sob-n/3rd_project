from django.shortcuts import render
from django.urls import path
from django.contrib.auth import views as auth_views

from interview import views

app_name = 'interview'

urlpatterns = [
    path('recording_1/', views.interview, name='interview'),
    path('recording_2/', views.interview1, name='interview1'),
    path('recording_3/', views.interview2, name='interview2'),
    path('recording_4/', views.interview3, name='interview3'),
    path('analysis_1/', views.analysis, name='analysis'),
    path('analysis_2/', views.analysis1, name='analysis1'),
    path('homepage_1/', views.homepage, name='homepage'),
]