from django.db import models
from django.contrib.auth.models import AbstractUser

class users(AbstractUser):
    final_school = models.CharField(max_length=90)
    major = models.CharField(max_length=90)
    degree = models.CharField(max_length=4)
    
