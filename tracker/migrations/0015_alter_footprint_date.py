# Generated by Django 4.1 on 2022-10-28 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0014_alter_footprint_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footprint',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
