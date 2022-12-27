from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home,name='home'),
    path('register/', views.registerPage,name='register'),
    path('login/', views.loginPage,name='login'),
    path('logout/', views.logoutPage,name='logout'),
    path('user/', views.userPage, name="user-page"),
    path('customer/<str:pk_test>/', views.customer,name='customer'),
    path('account/', views.accountSettings, name="account"),
    path('products/', views.products,name='products'),
    # path('create_orders/', views.order_create,name='create_order'),
    path('create_orders/<str:pk>/', views.order_create,name='create_order'),
    path('update_orders/<str:pk>/', views.update_order,name='update_order'),
    path('delete_orders/<str:pk>/', views.delete_order,name='delete_order'),
    # path('reset_password/',auth_views.PasswordResetView.as_view(),name="reset_password"),
    # path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    # path('reset/<uid64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    # path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"), 
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="account/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="account/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="account/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="account/password_reset_done.html"), 
        name="password_reset_complete"),
 
]
