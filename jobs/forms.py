from django import forms
from jobs.models import Job

class PostingForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['job_title', 'salary', 'qualification', 'job_description', 'process', 'deadline']
    