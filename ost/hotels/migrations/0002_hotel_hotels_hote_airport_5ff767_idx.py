# Generated by Django 4.2 on 2023-12-08 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='hotel',
            index=models.Index(fields=['airport_distance'], name='hotels_hote_airport_5ff767_idx'),
        ),
    ]
