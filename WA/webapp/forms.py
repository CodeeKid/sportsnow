from django import forms


class User(forms.Form):
    email = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
