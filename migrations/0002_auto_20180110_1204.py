# Generated by Django 2.0 on 2018-01-10 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_info',
            name='profilePicture',
        ),
        migrations.AddField(
            model_name='user_info',
            name='userProfilePicture',
            field=models.ImageField(default='C:/Users/Varun/Desktop/Images/defaultpicture.png', upload_to='C:/Users/Varun/Desktop/Images/'),
        ),
    ]