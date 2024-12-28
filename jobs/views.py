from django.shortcuts import render, redirect
from .forms import JobForm
from .models import Company, Job
from authentication.decorators import *

@login_required
def create_job(request):
    if request.method == 'POST':
        # Retrieve the company associated with the logged-in user
        company = Company.objects.filter(user=request.user).first()  # Use .first() to get the first result (or None if not found)

        # Create the form with POST data
        form = JobForm(request.POST)

        if form.is_valid():
            job = form.save(commit=False)
            job.company = company  # Link the job to the company of the logged-in user
            job.save()  # Save the job

            # Redirect to the home or job list page after successful job creation
            return redirect('home')  # Or redirect to a specific page where jobs are listed
        else:
            # If the form is not valid, print the form errors
            print("Form is invalid")
            print(form.errors)  # This will show you why the form is invalid

    else:
        # If the request is GET, create an empty form
        form = JobForm()

    # Render the form in the template
    return render(request, 'job-register.html', {'form': form})
