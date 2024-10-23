from django.shortcuts import render,redirect
from jobs.forms import PostingForm
from django.contrib import messages
from jobs.models import Job
from django.views.generic import DetailView,UpdateView
from django.urls import reverse_lazy

def post_a_job(request):
    if request.method == 'POST':
        form = PostingForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.company_name = request.user.username
            job.company_description = request.user.company_description
            job.location = request.user.location
            job.business_description = request.user.business_description
            job.capital = request.user.capital
            job.annual_sales = request.user.annual_sales
            job.number_of_employees = request.user.number_of_employees
            job.save()
            messages.success(request, "Job posted successfully!")
            return redirect('co_home')
    
    else:
        form = PostingForm()
    return render(request, 'post_a_job.html', {'form': form})

def jobs(request):
    if request.user.is_authenticated:
        company_name = request.user.username
        jobs = Job.objects.filter(company_name = company_name)
        return render(request, 'jobs.html', {'jobs': jobs})
    else:
        return redirect('co_login')

class detail(DetailView):
    model = Job
    template_name = 'detail.html'
    context_object_name = 'job'

class update(UpdateView):
    model = Job
    form_class = PostingForm
    template_name = 'update.html'
    success_url = reverse_lazy('jobs')
