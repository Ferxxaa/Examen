# Generated by Django 5.0.6 on 2024-07-05 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0010_remove_cliente_direccion_remove_cliente_telefono_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='total',
        ),
    ]
