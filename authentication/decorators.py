from functools import wraps
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.shortcuts import redirect,render
from jobs.models import Company

def login_required(view_func):
    '''
    used for authorization 
    '''
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/auth/register')
            return JsonResponse({'error':'unauthorized'},status=401)
        return view_func(request, *args, **kwargs)
    return _wrapped_view


def company_required(view_func):
    '''
    for some routes it is required for user to register a company first
    '''

    @wraps(view_func)
    def _wrapped_view(request,*args,**kwargs):
        company = Company.objects.filter(user=request.user)
        if not company:
            return redirect('home')
        return view_func(request, *args, **kwargs)
    return _wrapped_view