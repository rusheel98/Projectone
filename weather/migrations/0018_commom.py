# Generated by Django 2.0.4 on 2018-05-03 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0017_sensorreadings_ph'),
    ]

    operations = [
        migrations.CreateModel(
            name='commom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turb', models.CharField(max_length=30)),
                ('level', models.CharField(max_length=30)),
            ],
        ),
    ]