from django import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class User(forms.Form):
    email = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)


class Event(forms.Form):
    title = forms.CharField(max_length=100)
    subtitle = forms.CharField(max_length=100)
    date = forms.CharField(max_length=100)
    time = forms.CharField(max_length=100)


class Food(forms.Form):
    title = forms.CharField(max_length=100)
    image = forms.ImageField()


class CreateUserForm(UserCreationForm):

    model = User
    fields = ['username', 'email', 'password1', 'password2']
