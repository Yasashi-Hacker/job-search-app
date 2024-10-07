from django import forms
from .models import users

class SignUpForm(forms.ModelForm)
    class Meta:
        model = users
        fields = ['user_id', 'password', 'user_name', 'final_school', 'major', 'degree']
    
    password = forms.CharField(widget=forms.PasswordInput)
