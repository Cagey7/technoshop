from django.shortcuts import render
from django.views.generic.list import ListView
from .models import *
from core.views import navbar_auth, navbar_not_auth


class ProductsHome(ListView):
    template_name = "products/index.html"
    context_object_name = "items"
    extra_context = {
        "title": "Главная страница",
        "categories": Category.objects.all(),
        "navbar_auth": navbar_auth,
        "navbar_not_auth": navbar_not_auth
    }

    def get_queryset(self):
        return Item.published.all().select_related("item_category")


class ItemCategory(ListView):
    template_name = "products/index.html"
    context_object_name = "items"
    extra_context = {
        "navbar_auth": navbar_auth,
        "navbar_not_auth": navbar_not_auth,
        "categories": Category.objects.all()
    }

    def get_queryset(self):
        return Item.published.filter(item_category__slug=self.kwargs["category_slug"])
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        category = context["items"][0].item_category
        context["title"] = "Категория - " + category.name
        context["selected_category"] = category.pk
        return context
