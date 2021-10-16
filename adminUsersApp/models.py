from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AdminUser(User):
    age = models.IntegerField()

    class Meta:
        verbose_name = 'Admin User'
        verbose_name_plural = 'Admin Users'
