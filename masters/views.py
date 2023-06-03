from django.shortcuts import render, redirect
from order.models import Order
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required

# Create your views here.

def master_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password = password)
        if(user.get_username() == "master"):
            login(request, user)
            return redirect('view-orders')
        return HttpResponse("You are not master")
    return render(request, 'masters/login.html')

@login_required(login_url="master-login")
def view_orders(request):
    all_orders = Order.objects.all().order_by('order_priorty')
    return render(request, 'masters/all_orders.html', context={"all_orders":all_orders})

@login_required(login_url="master-login")
def view_perticular_order(request, id):
    order = Order.objects.get(id = id)
    return render(request, 'masters/single_order.html', context={"order":order})

@login_required(login_url="master-login")
def logout_master(request):
    logout(request)
    return render(request, 'masters/login.html')

@login_required(login_url="master-login")
def status_of_order(request, id):
    if request.method == "POST":
        if request.data["status"] == "Cutting Started".lower():
            pass
        if request.data["status"] == "Stiching Started".lower():
            pass
        if request.data["status"] == "Finished".lower():
            pass
    return redirect("view-perticular-order", id=id)