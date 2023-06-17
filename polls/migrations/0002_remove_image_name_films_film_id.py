# Generated by Django 4.2.2 on 2023-06-17 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='name',
        ),
        migrations.AddField(
            model_name='films',
            name='film_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.image'),
        ),
    ]
