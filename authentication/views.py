"""
This Module Is For User Authentication
"""

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from jobs.models import Company, Job
from jobs.forms import CompanyForm
from .forms import CustomUserCreationForm


def register(request):
    """
    This is for Registering User
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        print(form.errors)
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    """
    This is for login User
    """
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        return render(request, 'login.html', {'error': "Invalid email or Password"})
    return render(request, 'login.html')


@login_required
def home_view(request):
    """
    Home Screen
    """
    page_num = request.GET.get('page', 1)
    jobs = Job.objects.all()  # pylint: disable=no-member
    paginator = Paginator(jobs, 5)
    page_obj = paginator.get_page(page_num)
    jobs = page_obj.object_list

    if Company.objects.filter(user=request.user).exists():  # pylint: disable=no-member
        company = Company.objects.filter(user=request.user).first()  # pylint: disable=no-member
        res_obj = {'jobs': jobs, 'user': request.user, 'company': company, 'page_obj': page_obj}
        return render(request, 'home.html', res_obj)

    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.user = request.user
            company.save()
            res_obj = {'jobs': jobs, 'user': request.user, 'company': company, 'page_obj': page_obj}
            return render(request, 'home.html', res_obj)
        print(form.errors)
    form = CompanyForm()
    return render(request, 'company_registration.html', {'form': form})

@login_required
def logout_view(request):
    """
    Logout view
    """
    logout(request)
    return redirect('login')
