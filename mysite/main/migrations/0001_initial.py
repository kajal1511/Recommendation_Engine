# Generated by Django 3.0.5 on 2020-04-30 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('rating', models.FloatField()),
                ('img_src', models.TextField()),
                ('genre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('genre', models.TextField()),
                ('director', models.CharField(max_length=255)),
                ('stars', models.TextField()),
                ('rating', models.FloatField()),
                ('oscar', models.CharField(max_length=10)),
                ('duration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TVShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('genre', models.TextField()),
                ('stars', models.TextField()),
                ('rating', models.FloatField()),
                ('duration', models.IntegerField()),
            ],
        ),
    ]
