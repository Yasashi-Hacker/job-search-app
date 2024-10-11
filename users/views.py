from django.shortcuts import render, redirect
from users.forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'index.html', {})

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})
    
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            ID = form.cleaned_data['user_id']
            password = form.cleaned_data['password']
            user = authenticate(request, username=ID, password=password)
            if user is not None:
                login(request, user)
                return redirect('user_home')
            else:
                form.add_error(None, "Invalid ID or password.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form}) 

def user_home(request):
          return render(request, 'user_home.html', {})  


        