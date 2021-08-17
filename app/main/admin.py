from django.contrib import admin
from .models import Product, ProductImages, Category

class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    extra = 3

class ProductsAdmin(admin.ModelAdmin):
    inlines = [ ProductImagesInline, ]

admin.site.register(Product, ProductsAdmin)
admin.site.register(ProductImages)
admin.site.register(Category)
# Register your models here.
