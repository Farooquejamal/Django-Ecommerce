from django.contrib import admin
from .models import ShippingAddress,Order,OrderItem
from django.contrib.auth.models import User
# Register your models here.

admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(OrderItem)

class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 0

# Extend our order model
class OrderAdmin(admin.ModelAdmin):
    model = Order
    readonly_fields = ["date_ordered"]
    fields = ['user','full_name',"email",'shipping_address','amount_paid','date_ordered',"shipped",'date_shipped']
    inlines = [OrderItemInline]

# Unregister the Order model
admin.site.unregister(Order)

# Re-register the Order model
admin.site.register(Order,OrderAdmin)