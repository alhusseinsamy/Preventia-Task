from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NormalUser(User):
    age = models.IntegerField()

    class Meta:
        verbose_name = 'Normal User'
        verbose_name_plural = 'Normal Users'