# Generated by Django 3.2.3 on 2021-07-06 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_userdetail_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='phone_number',
            field=models.CharField(max_length=20, verbose_name='Номер мобильного телефона'),
        ),
    ]