# Generated by Django 3.0.8 on 2020-11-08 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_auto_20201108_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.IntegerField(blank=True, default='Unknown'),
        ),
    ]
