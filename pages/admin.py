from django.contrib import admin
from .models import Product



class ProductAdmin(admin.ModelAdmin):
    Model = Product
    #fields = ['name', 'price', 'is_discount', 'discount', 'discount_price']
    list_display = ('name', 'price', 'is_discount', 'discount')


admin.site.register(Product, ProductAdmin)