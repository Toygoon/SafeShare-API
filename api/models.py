from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=10)
    user_pw = models.CharField(max_length=50)
    name = models.CharField(max_length=10)
    mileage = models.PositiveIntegerField()
    mobile = models.CharField(max_length=50)