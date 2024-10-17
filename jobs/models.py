from django.db import models

class Job(models.Model):
    company_name = models.CharField(max_length=161, blank=True, null=True)
    company_description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    business_description = models.TextField(blank=True, null=True)
    capital = models.IntegerField(blank=True, null=True)
    annual_sales= models.IntegerField(blank=True, null=True)
    number_of_employees = models.IntegerField(blank=True, null=True)
    job_title = models.CharField(max_length=100)
    salary = models.IntegerField()
    qualification = models.TextField()
    job_description = models.TextField()
    process = models.TextField()
    deadline = models.DateTimeField()