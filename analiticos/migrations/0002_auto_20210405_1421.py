# Generated by Django 3.1.7 on 2021-04-05 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analiticos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivo',
            name='Excel',
            field=models.FileField(upload_to='archivos/excel/'),
        ),
    ]
