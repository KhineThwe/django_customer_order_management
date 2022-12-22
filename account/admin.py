from django.contrib import admin
from . models import Order,Customer,Product,Tag
# Register your models here.
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tag)