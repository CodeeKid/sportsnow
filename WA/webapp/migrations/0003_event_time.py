# Generated by Django 3.0.8 on 2020-08-04 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.TextField(default='', max_length=100),
        ),
    ]