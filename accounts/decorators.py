from django.shortcuts import redirect
from functools import wraps

def comment_login_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        return redirect('login')
    
    return wrapper


def already_login(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        
        return view_func(request, *args, **kwargs)
    
    return wrapper