# Generated by Django 4.2.2 on 2023-06-19 10:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='films',
            name='release_film',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 6, 19, 10, 28, 49, 699933)),
        ),
    ]