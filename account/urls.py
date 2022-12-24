from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('customer/<str:pk_test>/', views.customer,name='customer'),
    path('products/', views.products,name='products'),
    # path('create_orders/', views.order_create,name='create_order'),
    path('create_orders/<str:pk>/', views.order_create,name='create_order'),
    path('update_orders/<str:pk>/', views.update_order,name='update_order'),
    path('delete_orders/<str:pk>/', views.delete_order,name='delete_order'),
]
