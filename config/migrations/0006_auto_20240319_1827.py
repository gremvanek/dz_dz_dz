# Generated by Django 3.2.24 on 2024-03-19 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0005_auto_20240318_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата_создания'),
        ),
        migrations.AlterField(
            model_name='post',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(blank=True, max_length=200, unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='post',
            name='views_count',
            field=models.IntegerField(default=0, verbose_name='Просмотры'),
        ),
    ]