from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from .forms import CustomUserCreationForm


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

def home_view(request):
    return render(request,'home.html')
