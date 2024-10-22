from django.contrib import admin
from .models import Product,Category,Customer,Order,Profile
from django.contrib.auth.models import User
# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Profile)