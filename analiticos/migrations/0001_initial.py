# Generated by Django 3.1.7 on 2021-04-05 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Excel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreAr', models.CharField(default='', max_length=30)),
                ('Excel', models.FileField(upload_to='archivos/excel/')),
            ],
        ),
        migrations.CreateModel(
            name='Proceso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proceso', models.CharField(blank=True, default='', max_length=30)),
                ('pkl', models.FileField(default='', upload_to='archivos/modelos/')),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Archivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analiticos.excel')),
                ('Proceso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analiticos.proceso')),
            ],
        ),
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
                ('Excel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analiticos.excel')),
                ('Proceso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analiticos.proceso')),
            ],
        ),
    ]
