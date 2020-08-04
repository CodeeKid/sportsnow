from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class Event(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    date = models.CharField(max_length=100, default='')
    time = models.CharField(max_length=100, default='')

class Food (models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
