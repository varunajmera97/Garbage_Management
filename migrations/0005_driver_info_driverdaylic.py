# Generated by Django 2.0 on 2018-01-12 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20180112_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver_info',
            name='driverDayLIC',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
