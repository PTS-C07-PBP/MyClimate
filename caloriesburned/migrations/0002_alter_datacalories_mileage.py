# Generated by Django 4.1 on 2022-10-28 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caloriesburned', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datacalories',
            name='mileage',
            field=models.FloatField(default=0),
        ),
    ]
