# Generated by Django 3.2.3 on 2021-05-26 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directories', '0003_auto_20210523_0131'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Автора', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'verbose_name': 'Жанр', 'verbose_name_plural': 'Жанры'},
        ),
        migrations.AlterModelOptions(
            name='publisher',
            options={'verbose_name': 'Издательство', 'verbose_name_plural': 'Издательства'},
        ),
        migrations.AlterModelOptions(
            name='series',
            options={'verbose_name': 'Серию', 'verbose_name_plural': 'Серии'},
        ),
    ]
