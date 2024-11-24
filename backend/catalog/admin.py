from django.contrib import admin
from django.db.models import JSONField
from django.forms import Textarea

from .models import Category, Brand, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_category')
    search_fields = ('name',)
    list_filter = ('parent_category',)
    prepopulated_fields = {'name': ('name',)}

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ('name', 'country')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'brand', 'price', 'in_stock', 'created_at')
    search_fields = ('name', 'category__name', 'brand__name')
    list_filter = ('category', 'brand', 'in_stock')
    ordering = ('-created_at',)
    autocomplete_fields = ('category', 'brand')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {'fields': ('name', 'category', 'brand', 'price', 'description', 'image', 'in_stock')}),
        ('Advanced Options', {'fields': ('specifications',)}),
    )
    formfield_overrides = {
        JSONField: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }
