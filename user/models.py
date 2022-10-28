from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    calories = models.FloatField(null=True, blank=True)
    carbon = models.FloatField(null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username','first_name','last_name']

