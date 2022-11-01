# Generated by Django 4.1 on 2022-10-29 18:42

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_created', models.BooleanField(default=False)),
                ('image', models.URLField()),
                ('link', models.URLField()),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateField(default=datetime.date.today)),
                ('region', models.CharField(choices=[('global', 'Global'), ('africa', 'Africa'), ('middle east', 'Middle East'), ('europe', 'Europe'), ('americas', 'Americas'), ('asia pacific', 'Asia Pacific')], default='Global', max_length=255)),
                ('description', models.TextField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
