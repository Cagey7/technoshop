from django.contrib import admin
from .models import Order, Purchase, News


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "order_status", "address", "total")
    list_per_page = 10


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ("item", "quantity", "order")
    list_display_links = ("item", )
    list_per_page = 10


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("name", )
    list_per_page = 10
