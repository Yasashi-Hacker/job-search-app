from django.db import models

class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_title = models.CharField(max_length=100)
    salary = models.IntegerField()
    qualification = models.TextField()
    job_description = models.TextField()
    process = models.TextField()
    deadline = models.DateTimeField()