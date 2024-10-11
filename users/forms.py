from django import forms
from .models import users
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = users
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'final_school', 'major', 'degree']
    
    username=forms.CharField(max_length=151, label='ID')
    final_school = forms.CharField(max_length=90, label='final school')
    major = forms.CharField(max_length=90)
    degree = forms.CharField(max_length=4)

class LoginForm(forms.Form):
    user_id = forms.CharField(label = "ID", max_length=151, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)