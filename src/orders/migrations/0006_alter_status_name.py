# Generated by Django 3.2.3 on 2021-07-04 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20210702_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Статус'),
        ),
    ]
