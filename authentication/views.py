from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from .forms import CustomUserCreationForm
from .decorators import *
from jobs.forms import CompanyForm
from jobs.models import Company


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'register.html', {'form' : form})

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request,email=email,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html',{'error':"Invalid email or Password"})
    
    return render(request, 'login.html')

@login_required
def home_view(request):
    if Company.objects.filter(user = request.user).exists():
        return render(request,'home.html',{'jobs':'Company Registered','user':request.user})
    else:
        if request.method == 'POST':
            form = CompanyForm(request.POST)
            if form.is_valid():
                company = form.save(commit=False)
                company.user = request.user
                company.save()
                return render(request,'home.html',{'jobs':'','user':request.user})
            else:
                form = CompanyForm()
                return render(request,'company_registration.html',{'form':form})
        else:
            return render(request,'company_registration.html')

