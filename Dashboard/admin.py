from django.contrib import admin
from .models import Customer, Cart, CartItem, Company, Product
# Register your models here.

admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Product)
admin.site.register(Company)
