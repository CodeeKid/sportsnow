from django import forms


class User(forms.Form):
    email = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)


class Event (forms.Form):
    title = forms.CharField(max_length=100)
    date_time = forms.CharField(max_length=100)
