# Generated by Django 5.0.4 on 2024-04-08 18:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_remove_comment_likes_alter_comment_owner_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='likes',
            field=models.ManyToManyField(related_name='liked_movies', to=settings.AUTH_USER_MODEL),
        ),
    ]
