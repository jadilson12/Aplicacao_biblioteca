# Generated by Django 2.2.1 on 2019-05-30 20:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_auto_20190530_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='reservationbook',
            name='expireDate',
            field=models.CharField(default=datetime.datetime(2019, 6, 9, 17, 22, 17, 151771), editable=False, max_length=20),
        ),
    ]