from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    final_school = models.CharField(max_length=90, blank=True, null=True)
    major = models.CharField(max_length=90, blank=True, null=True)
    degree = models.CharField(max_length=8, blank=True, null=True)
    company_description = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    business_description = models.CharField(max_length=200, blank=True, null=True)
    capital = models.IntegerField(blank=True, null=True)
    annual_sales= models.IntegerField(blank=True, null=True)
    number_of_employees = models.IntegerField(blank=True, null=True)
    is_employer = models.BooleanField()
