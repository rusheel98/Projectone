# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-03 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0013_auto_20171103_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='latitude',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='plant',
            name='longitude',
            field=models.CharField(max_length=30),
        ),
    ]
