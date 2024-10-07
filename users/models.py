from django.db import models

class users(models.Model):
    user_id = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=20)
    user_name = models.CharField(max_length=30)
    final_school = models.CharField(max_length=90)
    major = models.CharField(max_length=90)
    degree = models.CharField(max_length=4)
