from django.urls import path
from django.shortcuts import redirect
from . import views

app_name = 'blog'

urlpatterns = [

    path('', views.home, name='home'),
]
