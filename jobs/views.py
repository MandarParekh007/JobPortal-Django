from django.shortcuts import render, get_object_or_404, redirect
from .forms import JobForm
from .models import Company, Job
from authentication.decorators import *

@login_required
def create_job(request):
    if request.method == 'POST':

        company = Company.objects.filter(user=request.user).first()  

        form = JobForm(request.POST)

        if form.is_valid():
            job = form.save(commit=False)
            job.company = company 
            job.save()  

        
            return redirect('home')
        else:
            print("Form is invalid")
            print(form.errors) 

    else:
        # If the request is GET, create an empty form
        form = JobForm()

    # Render the form in the template
    return render(request, 'job-register.html', {'form': form})


@login_required
def update_job(request, id):
    job = get_object_or_404(Job, id=id)

    if request.method == 'POST':
        form = JobForm(request.POST,instance=job)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        return render(request,'update-job.html',{'job':job})
    

@login_required
def delete_job(request, id):
    job = get_object_or_404(Job, id=id)

    job.delete()

    return redirect('home')
    



