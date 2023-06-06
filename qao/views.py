from django.shortcuts import render, redirect
from order.models import Order
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required

# Create your views here.

def check_quality_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password = password)
        if(user.get_username() == "QAofficer" or user.is_superuser):
            login(request, user)
            return redirect('check-quality')
        return HttpResponse("You are not Quality Assurance Officer")
    return render(request, 'qao/login.html')

@login_required(login_url="login-quality")
def check_quality(request):
    all_orders = Order.objects.all().order_by('order_priorty')
    if request.method == "POST":
        id = request.POST["order"]
        order = Order.objects.get(id = id)
        data = request.POST["check"]
        if data == "accepted":
            order.order_status = "QUALITY CHECK PASSED"
            order.save()
        elif data == "rejected":
            order.order_status = "QUALITY CHECK FAILED"
            order.save()
    return render(request, 'qao/all_orders.html', context={"all_orders":all_orders})

@login_required(login_url="login-quality")
def check_quality_logout(request):
    logout(request)
    return redirect('login-quality')
