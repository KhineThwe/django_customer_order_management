from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import Group
from . models import *
from . forms import *
from . filters import *
from . decorators import *

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            # form.save()
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(
                user = user,
            )
            messages.success(request,'Accounts was created for '+ username)
            return redirect('login')
    context = {'form':form}
    return render(request,"account/register.html",context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or Password invalid!')
    context = {}
    return render(request,"account/login.html",context)

def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url = 'login')
@admin_only
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

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['admin'])
def customer(request,pk_test):
    customer = Customer.objects.get(id = pk_test)
    
    orders = customer.order_set.all()#quering customer child obj from model field
    
    order_count = orders.count()
    
    myFilter = OrderFilter(request.GET,queryset=orders)
    orders = myFilter.qs
    context = {'customer':customer,'orders':orders,'order_count':order_count,'myFilter':myFilter}
    return render(request,"account/customer.html",context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    order = request.user.customer.order_set.all()
    total_orders = order.count()
    delivered = order.filter(status='Delivered').count()
    pending = order.filter(status='Pending').count()
    context = {'orders':order,'total_orders':total_orders,'delivered':delivered,'pending':pending}
    return render(request, 'account/user.html', context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['admin'])
def products(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,"account/products.html",context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['admin'])
def order_create(request,pk):
    OrderFormSet = inlineformset_factory(Customer,Order,fields=('product','status'),extra=10)
    customer = Customer.objects.get(id=pk)
    # form = OrderForm(initial={'customer':customer})
    formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
    if request.method == "POST":
        # form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST,instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('home')
    context = {'formset':formset}
    return render(request,"account/order_form.html",context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['admin'])
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

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['admin'])
def delete_order(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
         order.delete()
         return redirect('home')
    context = {'item':order}
    return render(request,"account/delete.html",context)
    