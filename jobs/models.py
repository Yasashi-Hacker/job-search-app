from django.db import models

class job_listings(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_title = models.CharField(max_length=100)
    salary = models.IntegerField
    qualification = models.CharField(max_length=255)
    job_description = models.CharField(max_length=255)
    process = models.CharField(max_length=255)