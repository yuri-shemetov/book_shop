# Generated by Django 3.2.3 on 2021-05-30 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directories', '0004_auto_20210526_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Автор(ы)'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=25, verbose_name='Название жанра'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='city',
            field=models.CharField(max_length=25, verbose_name='Город издания'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(max_length=25, verbose_name='Название издательства'),
        ),
        migrations.AlterField(
            model_name='series',
            name='series',
            field=models.CharField(max_length=30, verbose_name='Серия книги'),
        ),
    ]
