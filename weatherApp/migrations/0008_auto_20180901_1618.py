# Generated by Django 2.1 on 2018-09-01 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherApp', '0007_auto_20180901_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='time',
            field=models.DateTimeField(blank=True),
        ),
    ]
