from django.shortcuts import render, get_object_or_404, redirect
from .forms import JobForm
from .models import Company, Job, Tag
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

            tags = form.cleaned_data.get('tags')

            if tags:
                tag_list = [tag.strip() for tag in tags.split(',')]
                for tag in tag_list:
                    Tag.objects.get_or_create(tag=tag,job=job)

        
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
        form = JobForm(request.POST, instance=job)

        if form.is_valid():
            job = form.save()  

            
            tags = form.cleaned_data.get('tags')
            if tags:
                tag_list = [tag.strip() for tag in tags.split(',')] 

                Tag.objects.filter(job=job).delete()

                for tag in tag_list:
                    Tag.objects.get_or_create(tag=tag, job=job)

            return redirect('home')

    else:
        form = JobForm(instance=job)

    return render(request, 'update-job.html', {'form': form, 'job': job})

    

@login_required
def delete_job(request, id):
    job = get_object_or_404(Job, id=id)

    job.delete()

    return redirect('home')
    



