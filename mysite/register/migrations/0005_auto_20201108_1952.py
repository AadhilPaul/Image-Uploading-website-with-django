# Generated by Django 3.0.8 on 2020-11-08 14:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_auto_20201108_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
    ]
