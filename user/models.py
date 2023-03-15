from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    rol = models.CharField(max_length=250,null=True,blank=True)