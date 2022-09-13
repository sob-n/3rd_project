from django.shortcuts import render
from django.urls import path
from django.contrib.auth import views as auth_views


from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='accounts/register.html'), name='register')

]