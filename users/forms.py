from django import forms
from users.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'final_school', 'major', 'degree', 'is_employer']
    
    drop_degree=[('Bechelor', 'Bechelor'), ('Master', 'Master'), ('Ph.D.','Ph.D.')]
    username=forms.CharField(max_length=161, label='ID', required =True)
    first_name = forms.CharField(max_length=30, label='First name', required=True)
    last_name = forms.CharField(max_length=30, label='Last name', required=True)
    final_school = forms.CharField(max_length=90, label='Final school', required=True)
    major = forms.CharField(max_length=90, required=True)
    degree = forms.ChoiceField(choices=drop_degree, widget=forms.Select, required=True)
    is_employer = forms.BooleanField(widget=forms.HiddenInput(), initial=False, required=False)

class LoginForm(forms.Form):
    user_id = forms.CharField(label = "ID", max_length=161, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)