from django.contrib import admin
from django.urls import path, include
from .views import home, loginpage, registerpage

urlpatterns = [
    path('', home),
    path('register', registerpage),
    path('loginpage', loginpage),

]
