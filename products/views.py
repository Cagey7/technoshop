from django.db.models.base import Model as Model
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from cart.forms import AddToCartForm
from .models import *
from core.views import navbar_auth, navbar_not_auth


class ProductsHome(TemplateView):
    template_name = "products/index.html"
    extra_context = {
        "title": "Главная страница",
        "categories": Category.objects.all(),
        "navbar_auth": navbar_auth,
        "navbar_not_auth": navbar_not_auth,
        "form": AddToCartForm
    }
    
    def get_context_data(self, **kwargs):
        print(self.request.session)
        context =  super().get_context_data(**kwargs)
        items_anon = Item.published.all().select_related("item_category")
        items = []
        if self.request.user.is_authenticated:
            for item in items_anon:
                items.append({"item": item, "is_in_cart": item.is_in_cart(self.request.user)})
            context["items"] = items
        else:
            if self.request.session.get("cart"):
                for item in items_anon:
                    for session_item in self.request.session["cart"]:
                        in_cart = False
                        if session_item.get("item") == item.id:
                            items.append({"item": item, "is_in_cart": True})
                            in_cart = True
                            break
                    if not in_cart:
                        items.append({"item": item, "is_in_cart": False})
                context["items"] = items
            else:
                for item in items_anon:
                    items.append({"item": item, "is_in_cart": False})
                context["items"] = items
        context["items_anon"] = items_anon
        return context


class ItemCategory(TemplateView):
    template_name = "products/index.html"
    extra_context = {
        "navbar_auth": navbar_auth,
        "navbar_not_auth": navbar_not_auth,
        "categories": Category.objects.all(),
        "form": AddToCartForm
    }

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        items_anon = Item.published.filter(item_category__slug=self.kwargs["category_slug"])
        items = []
        if self.request.user.is_authenticated:
            for item in items_anon:
                items.append({"item": item, "is_in_cart": item.is_in_cart(self.request.user)})
            context["items"] = items
        else:
            if self.request.session.get("cart"):
                for item in items_anon:
                    for session_item in self.request.session["cart"]:
                        in_cart = False
                        if session_item.get("item") == item.id:
                            items.append({"item": item, "is_in_cart": True})
                            in_cart = True
                            break
                    if not in_cart:
                        items.append({"item": item, "is_in_cart": False})
                context["items"] = items
            else:
                for item in items_anon:
                    items.append({"item": item, "is_in_cart": False})
                context["items"] = items
        context["items_anon"] = items_anon
        category = Category.objects.get(slug=self.kwargs["category_slug"])
        context["title"] = "Категория - " + category.name
        context["selected_category"] = category.pk
        return context


class ShowItem(TemplateView):
    template_name = "products/item.html"
    slug_url_kwarg = "item_slug"
    extra_context = {
        "navbar_auth": navbar_auth,
        "navbar_not_auth": navbar_not_auth,
        "form": AddToCartForm
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item = Item.objects.get(slug=self.kwargs[self.slug_url_kwarg])
        context["title"] = item.name
        if self.request.user.is_authenticated:
            context["item"] = {"item": item, "is_in_cart": item.is_in_cart(self.request.user)}
        else:
            if self.request.session.get("cart"):
                for session_item in self.request.session["cart"]:
                    in_cart = False
                    if session_item.get("item") == item.id:
                        context["item"] = {"item": item, "is_in_cart": True}
                        in_cart = True
                        break
                if not in_cart:
                    context["item"] = {"item": item, "is_in_cart": False}
            else:
                context["item"] = {"item": item, "is_in_cart": False}

        return context
    
