from django.contrib import admin
from .models import Order, Purchase


@admin.register(Order)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("user", "order_status", "address")
    list_per_page = 10


@admin.register(Purchase)
class CartAdmin(admin.ModelAdmin):
    list_display = ("item", "quantity", "order")
    list_display_links = ("item", )
    list_per_page = 10
