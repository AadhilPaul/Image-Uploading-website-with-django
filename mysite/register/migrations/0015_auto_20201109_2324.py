# Generated by Django 3.0.8 on 2020-11-09 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0014_profile_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
