from django.contrib import admin

from products.models import ProductModel, CategoryModel


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
	list_display = ['name', 'created_at', 'product_cat']
	list_filter = ['created_at']
	search_fields = ['name', 'description']


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
	list_display = ['name', 'created_at']
	list_filter = ['created_at']
	search_fields = ['name']
