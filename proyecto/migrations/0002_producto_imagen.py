# Generated by Django 5.0.6 on 2024-06-27 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(default='productos/default.jpg', upload_to='productos/'),
        ),
    ]
