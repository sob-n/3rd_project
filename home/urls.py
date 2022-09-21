from django.contrib import admin
from django.urls import path, include

import home
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.main, name='main'),
]