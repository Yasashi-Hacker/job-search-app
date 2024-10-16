from django import forms
from users.models import User
from django.contrib.auth.forms import UserCreationForm

class CompanySignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'company_description', 'location', 'business_description', 'capital', 'annual_sales', 'number_of_employees', 'is_employer']
    
    username=forms.CharField(max_length=161, label='Company Name', required=True)
    company_description = forms.CharField(max_length=255, label='Company description', required=True)
    location = forms.CharField(max_length=200, required=True)
    business_description = forms.CharField(max_length=200, label='Business description', required=True)
    capital = forms.IntegerField(required=True)
    annual_sales= forms.IntegerField(label='Annual sales', required=True)
    number_of_employees = forms.IntegerField(label='Number of employees', required=True)
    is_employer = forms.BooleanField(widget=forms.HiddenInput(), initial=True, required=False)

class CompanyLoginForm(forms.Form):
    user_id = forms.CharField(label = "ID", max_length=161, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)