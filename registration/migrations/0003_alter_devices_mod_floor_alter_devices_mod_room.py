# Generated by Django 4.2.2 on 2023-06-22 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_devices_mod_floor_devices_mod_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devices_mod',
            name='floor',
            field=models.CharField(max_length=50, verbose_name='Этаж'),
        ),
        migrations.AlterField(
            model_name='devices_mod',
            name='room',
            field=models.CharField(max_length=50, verbose_name='Комната'),
        ),
    ]