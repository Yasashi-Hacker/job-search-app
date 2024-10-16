from django.shortcuts import render, redirect
from companies.forms import CompanySignUpForm, CompanyLoginForm
from django.contrib.auth import authenticate, login
from users.models import User
def for_employers(request):
    return render(request, 'for_employers.html', {})

def co_sign_up(request):
    if request.method == 'POST':
        form = CompanySignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('co_login')
    
    else:
        form = CompanySignUpForm()
    return render(request, 'co_sign_up.html', {'form': form})
    
def co_login(request):
    if request.method == 'POST':
        form = CompanyLoginForm(request.POST)
        if form.is_valid():
            ID = form.cleaned_data['user_id']
            password = form.cleaned_data['password']
            user = authenticate(request, username=ID, password=password)
            if user is not None and user.is_employer:
                login(request, user)
                return redirect('co_home')
            else:
                form.add_error(None, "Invalid ID or password.")
    else:
        form = CompanyLoginForm()
    return render(request, 'co_login.html', {'form': form})

def co_home(request):
    return render(request, 'co_home.html', {})