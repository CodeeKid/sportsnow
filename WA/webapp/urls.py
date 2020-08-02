from django.contrib import admin
from django.urls import path, include
from .views import home, loginpage

urlpatterns = [
    path('', home),
    path('loginpage', loginpage)
]
