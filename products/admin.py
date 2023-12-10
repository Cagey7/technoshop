from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "is_published", "post_photo", "item_category", "created", )
    list_display_links = ("name", )
    ordering = ("created", )
    list_editable = ("is_published", "item_category")
    list_per_page = 10
    actions = ("set_in_stock", "set_off_stock")
    search_fields = ("name", "item_category__name")
    list_filter = ("is_published", "item_category__name")
    readonly_fields = ("post_photo", )

    @admin.display(description="Просмотр")
    def post_photo(self, item):
        if item.photo.url:
            return mark_safe(f"<img src='{item.photo.url}' width=100>")
        return "Без фото"

    @admin.action(description="Опубликовать выбранный товар")
    def set_in_stock(self, request, queryset):
        count = queryset.update(is_published=Item.Status.IN_STOCK)
        self.message_user(request, f"Измененно {count} записей.")

    @admin.action(description="Снять с публикации выбранный товар")
    def set_off_stock(self, request, queryset):
        count = queryset.update(is_published=Item.Status.OFF_STOCK)
        self.message_user(request, f"Измененно {count} записей.")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "post_photo")
    list_display_links = ("name", )
    readonly_fields = ("post_photo", )

    @admin.display(description="Просмотр")
    def post_photo(self, category):
        if category.photo.url:
            return mark_safe(f"<img src='{category.photo.url}' width=100>")
        return "Без фото"
