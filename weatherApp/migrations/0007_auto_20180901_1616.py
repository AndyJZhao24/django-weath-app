# Generated by Django 2.1 on 2018-09-01 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherApp', '0006_location_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='time',
            field=models.DateField(blank=True),
        ),
    ]
