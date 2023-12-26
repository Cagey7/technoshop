from django.db.models.base import Model as Model
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
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
    allow_empty = False
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


class ShowItem(DetailView):
    model = Item
    template_name = "products/item.html"
    slug_url_kwarg = "item_slug"
    context_object_name = "item"
    extra_context = {
        "navbar_auth": navbar_auth,
        "navbar_not_auth": navbar_not_auth
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = context["item"].name
        return context
    
    def get_object(self, queryset=None):
        return get_object_or_404(Item.published, slug=self.kwargs[self.slug_url_kwarg])
