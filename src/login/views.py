from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.utils.timezone import now
from .documents import UserDocument
from django.contrib.auth.models import User
from django.contrib import messages




def log_login_attempt(username, success, ip_address):
    user_log = UserDocument(
        username=username,
        last_login_attempt=now(),
        login_success=success,
        ip_address=ip_address
    )
    user_log.save()

def login_form(request):
    return render(request, 'login/vulnerable_login.html')

def vulnerable_login(request):
    ip_address = request.META.get('REMOTE_ADDR')
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        try:
            user = User.objects.get(username=username)
            if user.password == password:
                login(request, user)
                messages.success(request, 'Inicio de sesión exitoso.')
                return redirect('dashboard')
        except User.DoesNotExist:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'login/vulnerable_login.html')

def custom_logout(request):
    logout(request)
    return render(request, 'login/logout.html')