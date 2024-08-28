# Generated by Django 5.1 on 2024-08-27 09:55

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0017_remove_image_camera_remove_image_film_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=5000, null=True)),
                ('manufacturer', models.CharField(blank=True, max_length=5000, null=True)),
                ('modell', models.CharField(blank=True, max_length=5000, null=True)),
                ('first_production', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=5000, null=True)),
                ('iso', models.IntegerField(blank=True, null=True)),
                ('manufacturer', models.CharField(blank=True, max_length=5000, null=True)),
                ('first_production', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Lens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=5000, null=True)),
                ('manufacturer', models.CharField(blank=True, max_length=5000, null=True)),
                ('modell', models.CharField(blank=True, max_length=5000, null=True)),
                ('focallength', models.CharField(blank=True, max_length=5000, null=True)),
                ('aperature', models.CharField(blank=True, max_length=5000, null=True)),
                ('first_production', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Scanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=5000, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='camera',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.camera'),
        ),
        migrations.AddField(
            model_name='image',
            name='film',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.film'),
        ),
        migrations.AddField(
            model_name='camera',
            name='lens',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.lens'),
        ),
        migrations.AddField(
            model_name='image',
            name='lens',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.lens'),
        ),
        migrations.AddField(
            model_name='image',
            name='scanner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.scanner'),
        ),
    ]
