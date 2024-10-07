from django.db import models

class jobs(models.Model):
    job_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=161)
    job_title = models.CharField(max_length=100)
    salary = models.IntegerField
    location = models.CharField(max_length=200)
    qualification = models.CharField(max_length=500)
    job_description = models.CharField(max_length=500)
    process = models.CharField(max_length=500)
    company_profile = models.CharField(max_length=500)