# Generated by Django 3.1.7 on 2021-04-08 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analiticos', '0003_auto_20210405_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='archivo',
            name='Proceso',
        ),
    ]
