from django.shortcuts import render
from django.urls import path
from django.contrib.auth import views as auth_views

from interview import views

app_name = 'interview'

urlpatterns = [
    # path('recording_1/', views.interview1, name='interview1'),
    # path('recording_2/', views.interview2, name='interview2'),
    # path('recording_3/', views.interview3, name='interview3'),
    # path('recording_4/', views.interview4, name='interview4'),
    path('recording/<int:page_num>', views.interview, name='recording'),
    path('analysis/', views.analysis, name='analysis'),

]