# Generated by Django 5.0.4 on 2024-04-13 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_movie_imdb_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='title',
        ),
    ]
