from django.shortcuts import render,redirect
from jobs.forms import PostingForm
from django.contrib import messages

def post_a_job(request):
    if request.method == 'POST':
        form = PostingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Job posted successfully!")
            return redirect('co_home')
    
    else:
        form = PostingForm()
    return render(request, 'post_a_job.html', {'form': form})

def jobs(request):
    return render(request, 'jobs.html', {})

