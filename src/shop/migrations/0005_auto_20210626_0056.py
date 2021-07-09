# Generated by Django 3.2.3 on 2021-06-25 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directories', '0005_auto_20210530_1945'),
        ('shop', '0004_promo_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(related_name='Автор', to='directories.Author', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Жанр', to='directories.genre', verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Издательство', to='directories.publisher', verbose_name='Издательство'),
        ),
        migrations.AlterField(
            model_name='book',
            name='seria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Серия', to='directories.series', verbose_name='Серия'),
        ),
    ]
