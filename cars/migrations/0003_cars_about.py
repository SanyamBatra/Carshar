# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-01 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_cars_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='about',
            field=models.TextField(default=' '),
        ),
    ]
