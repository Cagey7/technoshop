from django.contrib import admin
from .models import CartItem, Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("user", )
    list_per_page = 10


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("item", "quantity", "cart")
    list_display_links = ("item", )
    list_per_page = 10
