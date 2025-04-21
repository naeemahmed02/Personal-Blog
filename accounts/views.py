from django.shortcuts import render, redirect
from django.contrib.auth import  authenticate, login, logout
from django.contrib import messages
from utils.utils import validate_passwords
from . models import CustomUser
from . decorators import already_login


@already_login
def login_page(request):

    next_url = request.GET.get('next') or request.POST.get('next') or '/'

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')

        user = authenticate(request, email = email, password = password)
        
        if user is not None:
            login(request, user=user)
            
            if remember_me != 'on':
                request.session.set_expiry(0)
            else:
                # request.session.set_expiry(86400)
                request.session.set_expiry(60)

            return redirect(next_url)
        else:
            messages.error(request, 'Invalid Email or Password')
    return render(request, 'login.html', {'next': next_url})

@already_login
def register(request):
    if request.method == "POST":
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Basic Validations
        if CustomUser.objects.filter(email = email).exists():
            messages.error(request, "Email is Already registered.")
            return redirect('register')
        
        # Custom Password Validation
        is_valid, message = validate_passwords(password, confirm_password)
        if not is_valid:
            messages.error(request, message)
            return redirect('register')
        
        user = CustomUser.objects.create_user(
            email=email, first_name= first_name,
              last_name = last_name, password=password)
        user.save()
        return redirect('login')

    return render(request, 'register.html')


def logout_page(request):
    logout(request)
    return redirect('login')












