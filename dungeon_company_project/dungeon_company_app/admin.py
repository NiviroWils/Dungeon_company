from django.contrib import admin
from .models import Product, Order


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'game_rules')

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)