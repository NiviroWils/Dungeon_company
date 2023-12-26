from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'game_rules')

admin.site.register(Product, ProductAdmin)