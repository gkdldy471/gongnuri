from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('detail/', views.detail, name='detail'),
    path('waiting/', views.waiting, name='waiting'),
    path('base/', views.base, name='base'),
    path('', views.home, name='home')
]