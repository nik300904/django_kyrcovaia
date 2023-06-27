# Generated by Django 4.2.2 on 2023-06-27 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('film', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.films')),
            ],
        ),
    ]