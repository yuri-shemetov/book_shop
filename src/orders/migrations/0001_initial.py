# Generated by Django 3.2.3 on 2021-06-27 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carts', '0004_alter_bookincart_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_info', models.TextField(verbose_name='Contact info')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Update')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='carts.cart', verbose_name='Order')),
            ],
        ),
    ]