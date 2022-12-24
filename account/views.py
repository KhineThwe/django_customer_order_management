from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.forms import inlineformset_factory
from . models import *
from . forms import *

def home(request):
    order = Order.objects.all()
    customer = Customer.objects.all()
    total_customers = customer.count()
    total_orders = order.count()
    delivered = order.filter(status='Delivered').count()
    pending = order.filter(status='Pending').count()
    
    context = {'order':order,'customer':customer,'total_customers':total_customers
               ,'total_orders':total_orders,'delivered':delivered,'pending':pending}
    return render(request,"account/dashboard.html",context)

def customer(request,pk_test):
    customer = Customer.objects.get(id = pk_test)
    
    orders = customer.order_set.all()#quering customer child obj from model field
    
    order_count = orders.count()
    context = {'customer':customer,'orders':orders,'order_count':order_count}
    return render(request,"account/customer.html",context)

def products(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,"account/products.html",context)

def order_create(request,pk):
    customer = Customer.objects.get(id=pk)
    form = OrderForm(initial={'customer':customer})
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request,"account/order_form.html",context)

def update_order(request,pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == "POST":
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request,"account/order_form.html",context)

def delete_order(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
         order.delete()
         return redirect('home')
    context = {'item':order}
    return render(request,"account/delete.html",context)
    