from django.contrib import admin
from django.urls import path
from . import views
import account.views

urlpatterns = [
    path('signup/', account.views.signup, name='signup'),
    path('login/', account.views.login, name='login'),
    path('logout/', account.views.logout, name='logout'),
]