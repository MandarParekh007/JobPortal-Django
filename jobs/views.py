from django.shortcuts import render, get_object_or_404, redirect
from .forms import JobForm
from .models import Company, Job, Tag
from authentication.decorators import *

@login_required
@company_required
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
@company_required
def update_job(request, id):
    job = get_object_or_404(Job, id=id)

    company = Company.objects.filter(user=request.user).first()
    if job.company != company:
        return JsonResponse({'error':'401','message':'something went wrong'})


    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)

        if form.is_valid():
            job = form.save()  # Save the updated job

            # Process the tags input from the form
            tags = form.cleaned_data.get('tags')
            if tags:
                tag_list = [tag.strip() for tag in tags.split(',')]  # Split and clean the tags

                # Remove existing tags for this job
                Tag.objects.filter(job=job).delete()

                # Add new tags
                for tag in tag_list:
                    Tag.objects.get_or_create(tag=tag, job=job)

            return redirect('home')
        else:
            print(form.errors)

        # If the form is invalid, return the same page with error messages
        return render(request, 'update-job.html', {'form': form, 'job': job})

    else:
        # For GET request, fetch existing tags for this job
        tags = Tag.objects.filter(job=job)  # Get tags associated with the job
        form = JobForm(instance=job)

        # Always pass 'tags' to the template, whether it's a POST or GET request
        return render(request, 'update-job.html', {'form': form, 'job': job, 'tags': tags})




    

@login_required
@company_required
def delete_job(request, id):
    
    job = get_object_or_404(Job, id=id)

    company = Company.objects.filter(user=request.user).first()
    if job.company != company:
        return JsonResponse({'error':'401','message':'something went wrong'})

    job.delete()

    return redirect('home')
    



