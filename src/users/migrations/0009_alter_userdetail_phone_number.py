# Generated by Django 3.2.3 on 2021-07-01 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20210628_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Номер мобильного телефона'),
        ),
    ]
