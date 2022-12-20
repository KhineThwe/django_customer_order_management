from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    return render(request,"account/dashboard.html")

def customer(request):
    return render(request,"account/customer.html")

def products(request):
    return render(request,"account/products.html")