# Generated by Django 5.1 on 2024-08-31 22:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0039_camera_color_variants_alter_camera_modes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='html_template',
            field=models.CharField(blank=True, choices=[('article_template01.html', 'Story, links Text, rechts Bilder'), ('article_template02.html', 'Artikel, links Text, rechts Bilder'), ('article_template03.html', 'Artikel, Text, Bild, Tabelle')], max_length=5000),
        ),
        migrations.AlterField(
            model_name='articlelinker',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='linked_article', to='posts.article'),
        ),
        migrations.AlterField(
            model_name='camera',
            name='modes',
            field=models.CharField(blank=True, choices=[('Vollautomatisch', 'Vollautomatisch'), ('Programm', 'Programm'), ('Blendenautomatik', 'Blendenautomatik'), ('Belichtungsautomatik', 'Belichtungsautomatik'), ('Manuell', 'Manuell'), ('Belichtungsautomatik und Vollautomatisch', 'Belichtungsautomatikundvollautomatisch'), ('Blendenautomatik und Vollautomatisch', 'Blendenautomatikundvollautomatisch')], max_length=100, null=True),
        ),
    ]
