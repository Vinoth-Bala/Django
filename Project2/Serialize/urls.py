from django.contrib import admin
from django.urls import URLPattern, path
from .import views

urlpatterns = [

    path('stu_data/', views.StuDetails.as_view()),
    path('dept_data/', views.DepDetails.as_view())

]