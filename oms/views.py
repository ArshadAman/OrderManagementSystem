from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib import messages

def homepage(request):
    return render(request, 'index.html')

def create_super_user(request):
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            User = get_user_model()
            if not User.objects.filter(is_superuser=True).exists():
                User.objects.create_superuser(username, email, password)
                return redirect(reverse('admin:index'))
            else:
                print("superuser already exits")
                messages.error(request, 'Superuser already exits')
                return redirect('create-admin')
    return render(request, "create_admin.html")