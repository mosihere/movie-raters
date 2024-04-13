# Generated by Django 5.0.4 on 2024-04-07 10:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('imdb_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('director', models.CharField(blank=True, max_length=255, null=True)),
                ('stars', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.star')),
            ],
        ),
    ]