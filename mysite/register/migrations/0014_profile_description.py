# Generated by Django 3.0.8 on 2020-11-08 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0013_auto_20201108_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.TextField(blank=True, default='This user has no description'),
        ),
    ]
