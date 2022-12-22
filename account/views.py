from django.shortcuts import render
from django.http import HttpRequest
from . models import *

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

def customer(request):
    return render(request,"account/customer.html")

def products(request):
    products = Product.objects.all()
    return render(request,"account/products.html",{'products':products})