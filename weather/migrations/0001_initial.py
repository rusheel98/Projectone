# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-13 14:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sensorreadings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.CharField(max_length=30)),
                ('humd', models.CharField(max_length=50)),
            ],
        ),
    ]
