from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path("UserData/",views.userdetails.as_view())
    

]