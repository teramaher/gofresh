from django.contrib import admin
from .models import Category, Product, User


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(User)
class UserList(admin.ModelAdmin):
    list_display = ('user_first_name', 'user_last_name', 'user_status')
    list_filter = ('user_first_name', 'user_last_name', 'user_status')
    search_fields = ('user_first_name', 'user_last_name')
    ordering = ['user_first_name']
