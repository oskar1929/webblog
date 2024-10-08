# Generated by Django 5.1 on 2024-08-30 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0027_imagecluster_alter_article_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='images',
            field=models.ManyToManyField(blank=True, null=True, related_name='articles', to='posts.image'),
        ),
    ]
