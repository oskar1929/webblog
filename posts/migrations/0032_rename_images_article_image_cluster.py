# Generated by Django 5.1 on 2024-08-30 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0031_remove_imagecluster_title_alter_imagecluster_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='images',
            new_name='image_cluster',
        ),
    ]
