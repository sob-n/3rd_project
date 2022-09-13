from django.contrib import admin
from django.urls import path, include

import mainapp
from . import views

urlpatterns = [

    path('mainapp/', views.main, name='main'),


]