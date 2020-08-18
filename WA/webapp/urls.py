from django.contrib import admin
from django.urls import path, include
from .views import home, loginpage, registerpage, book, pagelogout,simple_checkout,thankyou

urlpatterns = [
    path('', home),
    path('register/', registerpage),
    path('loginpage/', loginpage),
    path('book/<int:id>', book),
    path('logout', pagelogout),
    path('accounts/', include('django.contrib.auth.urls')),
    path('simplecheckout', simple_checkout),
    path('thankyou/<int:mid>', thankyou)

]
