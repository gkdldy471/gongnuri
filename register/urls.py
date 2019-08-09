from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('complete/', views.complete, name='complete'),
    path('place/', views.place, name='place'),
    path('create/',views.create, name='create'),
    path('place/<int:building_id>/', views.place_detail,name='place_detail'),
]