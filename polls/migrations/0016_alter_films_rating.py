# Generated by Django 4.2.2 on 2023-06-25 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_alter_films_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='films',
            name='rating',
            field=models.FloatField(),
        ),
    ]
