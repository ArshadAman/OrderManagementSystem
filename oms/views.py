from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import get_user_model, authenticate, login, logout
# from django.contrib.auth.hashers import make_password, check_password


def homepage(request):
    return render(request, 'index.html')

def create_super_user(request):
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            print(email, username, password, confirm_password)
            User = get_user_model()
            User.objects.create_superuser(username, email, password)
            return redirect(reverse('admin:index'))
    return render(request, "create_admin.html")

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            print(user.username)
            return redirect(reverse('admin:index'))
    return render(request, 'user_login.html')