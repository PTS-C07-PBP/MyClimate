# Generated by Django 4.1 on 2022-10-27 15:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0008_alter_footprint_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footprint',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
