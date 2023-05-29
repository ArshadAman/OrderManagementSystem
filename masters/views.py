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

def status_of_order(request):
    # Master will change the stats of order by clicking buttons, and on click the mail will be sent to the admin that the master has stated working on the order for example the master has started cutting the clothes or he has started stiching the clothes or he has finished the order and accordingly the admin will the order status and the customer will recieve the mail regarding that. I still dont know how to implement that feature, like I know the logic not the process. I dont know why I am writing this but I am enjoying this. Ok see you tada bye bye... I will code you tommorow dear status of order.
    pass