from django.shortcuts import render, redirect
from main import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages



# >>>>>>> log-in <<<<<<<---
def log_in(request):
    """log in """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard:staf_list')
        else:
            return render(request, 'dashboard/auth/error.html')
    else:
        return render(request, 'dashboard/auth/login.html')
    

# >>>>>>> log-out <<<<<-----
def log_out(request):
    """log out """
    logout(request)
    return redirect('auth:error')


# >>>>>>> error <<<<<<<------
def error(request):
    """ error message"""
    return render(request, 'dashboard/auth/error.html')


# >>>>>>> profile <<<<<-----
@login_required(login_url='dashboard:register')
def profil(request):
    """profil page"""
    
    return render(request, 'dashboard/profil/profile.html')



# >>>>>>> settings <<<<<< ----
@login_required(login_url='auth:login')
def setting(request):
    """settings page"""
    if request.method == 'POST':
        try:
            user = request.user
            user.username = request.POST['username']
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            messages.success(request, 'Profil  muvoffaqiyatli o`zgartirildi')
            user.save()
            return redirect('dashboard:staf_list')
        except:
            messages.error(request, 'Profil  muvoffaqiyatli o`zgartirilmadi')
    return render(request, 'dashboard/profil/setting.html')


# >>>>>>> edit-password <<<<<<
@login_required(login_url='auth:login')
def edit_password(request):
    """edit password page"""
    try:
        user = request.user
        password = request.POST.get('password')
        password_new = request.POST.get('password_new')
        password_conf = request.POST.get('password_conf')
        messages.success(request, ' password muvafaqiyatli ozgartirildi')
        if user.check_password(password) and password_new == password_conf:
            user.set_password(password_new)
            user.save()
        return redirect('dashboard:staf_list')
    except:
        messages.error(request, 'Password muvafaqiyatsz xatolik')