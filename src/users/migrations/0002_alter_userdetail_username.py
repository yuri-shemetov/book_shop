# Generated by Django 3.2.3 on 2021-06-22 08:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='username',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='Логин', to=settings.AUTH_USER_MODEL),
        ),
    ]
