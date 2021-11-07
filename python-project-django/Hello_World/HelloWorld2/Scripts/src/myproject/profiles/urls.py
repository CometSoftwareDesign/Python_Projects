from django.shortcuts import render
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views
from .models import Profiles

urlpatterns = [
    path('admin_console', views.admin_console, name = "admin_console"),
    path('<int:pk>/details/', views.details, name="details"),
]