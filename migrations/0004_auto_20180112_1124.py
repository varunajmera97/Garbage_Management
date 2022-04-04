# Generated by Django 2.0 on 2018-01-12 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20180110_1256'),
    ]

    operations = [
        migrations.CreateModel(
            name='driver_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driverProfilePicture', models.ImageField(default='C:/Users/varun/Desktop/Images/defaultpicture.png', upload_to='C:/Users/varun/Desktop/Project/garbagemanagement/DriverImages/')),
                ('driverName', models.CharField(max_length=25)),
                ('driverDayDOB', models.IntegerField()),
                ('driverMonthDOB', models.IntegerField()),
                ('driverYearDOB', models.IntegerField()),
                ('driverAddress', models.TextField()),
                ('driverEmail', models.CharField(max_length=25)),
                ('driverPhno', models.BigIntegerField()),
                ('driverUname', models.CharField(max_length=25)),
                ('driverPwrd', models.CharField(max_length=25)),
                ('driverMonthLIC', models.IntegerField()),
                ('driverYearLIC', models.IntegerField()),
                ('driverLino', models.CharField(max_length=15)),
                ('driverVeno', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='user_info',
            name='userProfilePicture',
            field=models.ImageField(default='C:/Users/varun/Desktop/Images/defaultpicture.png', upload_to='C:/Users/varun/Desktop/Project/garbagemanagement/UserImages/'),
        ),
    ]