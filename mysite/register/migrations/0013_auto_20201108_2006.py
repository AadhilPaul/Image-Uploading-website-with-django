# Generated by Django 3.0.8 on 2020-11-08 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0012_auto_20201108_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
