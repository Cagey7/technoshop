from django.db.models.base import Model as Model
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from .models import *
from sales.models import News
from products.models import Brand
from core.views import navbar_auth, navbar_not_auth


class ProductsHome(TemplateView):
    template_name = "products/index.html"
    extra_context = {
        "title": "Главная страница",
        "categories": Category.objects.all(),
        "chapters": Chapter.objects.all(),
        "news": News.objects.all(),
        "brands": Brand.objects.all(),
        "navbar_auth": navbar_auth,
        "navbar_not_auth": navbar_not_auth,
    }


class ItemCategory(TemplateView):
    template_name = "products/chapter.html"
    extra_context = {
        "navbar_auth": navbar_auth,
        "navbar_not_auth": navbar_not_auth,
        "chapters": Chapter.objects.all(),
    }

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        items_anon = Item.published.filter(item_category__slug=self.kwargs["category_slug"])
        category = Category.objects.get(slug=self.kwargs["category_slug"])

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
        context["categories"] = Category.objects.filter(category_chapter=category.category_chapter)
        context["title"] = "Категория - " + category.name
        context["selected_category"] = category.pk
        return context


class ShowItem(TemplateView):
    template_name = "products/item.html"
    slug_url_kwarg = "item_slug"
    extra_context = {
        "navbar_auth": navbar_auth,
        "navbar_not_auth": navbar_not_auth,
        "chapters": Chapter.objects.all(),
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
    

class ChapterInfo(TemplateView):
    template_name = "products/chapter.html"
    extra_context = {
        "chapters": Chapter.objects.all(),
        "navbar_auth": navbar_auth,
        "navbar_not_auth": navbar_not_auth,
    }

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["categories"] = Category.objects.filter(category_chapter__slug=self.kwargs["chapter_slug"])
        items_anon = Item.published.filter(item_category__in=context["categories"])
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
