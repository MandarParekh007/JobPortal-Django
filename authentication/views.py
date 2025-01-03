from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from .forms import CustomUserCreationForm
from .decorators import *
from jobs.forms import CompanyForm
from jobs.models import Company, Job
from django.core.paginator import Paginator


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
        else:
            print(form.errors)
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
    page_num = request.GET.get('page',1)
    jobs = Job.objects.all()
    p = Paginator(jobs,5)
    jobs = p.page(page_num).object_list
    page_obj = p.get_page(page_num)

    if Company.objects.filter(user = request.user).exists():
        company = Company.objects.filter(user = request.user)[0]
        return render(request,'home.html',{'jobs':jobs,'user':request.user,'company':company,'page_obj':page_obj})
    else:
        if request.method == 'POST':
            form = CompanyForm(request.POST)
            if form.is_valid():
                company = form.save(commit=False)
                company.user = request.user
                company.save()
                return render(request,'home.html',{'jobs':jobs,'user':request.user,'company':company,'page_obj':page_obj})
            else:
                print(form.errors)
                form = CompanyForm()
                form.errors = 'invalid Email or Password'
                return render(request,'company_registration.html',{'form':form})
        else:
            return render(request,'company_registration.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')