# Generated by Django 3.0.8 on 2020-08-04 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20200804_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.CharField(default='', max_length=100),
        ),
    ]