# Generated by Django 5.1 on 2024-09-02 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0042_alter_article_intro_text'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ArticleText',
        ),
    ]
