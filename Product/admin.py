from django.contrib import admin

# Register your models here.

from .models import *


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 1

class ProductColorInline(admin.TabularInline):
    model = ProductColor
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'discount_price', 'slug', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', 'price', 'discount_price', 'slug', 'created_at', 'updated_at')

    inlines = [
        ProductSizeInline,
        ProductColorInline,
        ProductImageInline,
    ]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(BannerImage)
class BannerImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_special')
