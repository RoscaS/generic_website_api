# Generated by Django 2.0.6 on 2018-08-24 19:11

import apps.gallery.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=100, null=True)),
                ('limit', models.IntegerField(default=8)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(upload_to=apps.gallery.models.gallery_path)),
                ('description', models.TextField(max_length=1000, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('position', models.PositiveIntegerField(default=0)),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='gallery.Gallery')),
            ],
        ),
    ]
