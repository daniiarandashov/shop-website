from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price')
    list_display_links = ('product_name',)
    search_fields = ('product_name', 'price')


admin.site.register(Product, ProductAdmin)
