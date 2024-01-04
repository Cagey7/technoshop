from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import DeleteView
from django.views import View
from .models import Cart, CartItem
from products.models import Item
from core.views import navbar_auth, navbar_not_auth


class AddToCart(View):
    def post(self, request, *args, **kwargs):
        item = get_object_or_404(Item, id=self.kwargs["item_id"])
        if self.request.user.is_authenticated:
            cart = Cart.objects.get(user__id=self.request.user.id)
            cart_item = CartItem(quantity=1, cart=cart, item=item)
            cart_item.save()
        else:
            if not self.request.session.get("cart"):
                self.request.session["cart"] = []
            self.request.session["cart"].append({"item": item.id, "quantity": 1})
        return redirect(self.get_success_url())

    def get_success_url(self):
        referer = self.request.META.get("HTTP_REFERER")
        if referer:
            return referer
        else:
            return reverse_lazy("index")


class CartPage(TemplateView):
    template_name = "cart/cart.html"
    extra_context = {
        "title": "Корзина",
        "navbar_auth": navbar_auth,
        "navbar_not_auth": navbar_not_auth,
    }

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            cart = Cart.objects.get(user=self.request.user)
            cart_items = CartItem.objects.filter(cart=cart).order_by("id")
            for cart_item in cart_items:
                item_id = cart_item.item.pk
                amount_available = Item.objects.get(id=item_id).quantity
                amount_in_cart = cart_item.quantity
                if amount_in_cart > amount_available:
                    cart_item.quantity = amount_available
                    cart_item.save()
                if amount_in_cart == 0 and amount_available > 0:
                    cart_item.quantity = 1
                    cart_item.save()
            context["cart_items"] = cart_items
        else:
            if self.request.session.get("cart"):
                new_cart = []
                new_session_cart = []
                cart = self.request.session["cart"]
                for item in cart:
                    item_id = item["item"]
                    amount_available = Item.objects.get(id=item_id).quantity
                    amount_in_cart = item["quantity"]
                    if amount_in_cart > amount_available:
                        quantity = amount_available
                    elif amount_in_cart == 0 and amount_available > 0:
                        quantity = 1
                    else:
                        quantity = item["quantity"]
                    new_cart.append({"item": Item.objects.filter(id=item_id), "quantity": quantity})
                    new_session_cart.append({"item": item_id, "quantity": quantity})
                context["cart_items"] = new_cart
                self.request.session["cart"] = new_session_cart
            else:
                context["cart_items"] = None
        return context


class DeleteItemCart(DeleteView):
    model = CartItem
    success_url = reverse_lazy("cart")


class DeleteItemCartAnon(View):
    def post(self, request, *args, **kwargs):
        cart = self.request.session["cart"]
        item_id  = kwargs.get("pk")
        new_cart = [item for item in cart if item["item"] != item_id]
        self.request.session["cart"] = new_cart
        return redirect("cart")


class IncreaseQuantity(View):
    def post(self, request, *args, **kwargs):
        cart_item = get_object_or_404(CartItem, id=kwargs.get("pk"))
        cart_item.increase_quantity()
        return redirect("cart")


class DecreaseQuantity(View):
    def post(self, request, *args, **kwargs):
        cart_item = get_object_or_404(CartItem, id=kwargs.get("pk"))
        cart_item.decrease_quantity()
        return redirect("cart")


class IncreaseQuantityAnon(View):
    def post(self, request, *args, **kwargs):
        cart = self.request.session["cart"]
        item_id=kwargs.get("pk")
        amount_available = Item.objects.get(id=item_id).quantity
        for item in cart:
            if item["item"] == item_id:
                if item["quantity"] < amount_available:
                    item["quantity"] += 1
                break
        return redirect("cart")


class DecreaseQuantityAnon(View):
    def post(self, request, *args, **kwargs):
        cart = self.request.session["cart"]
        item_id=kwargs.get("pk")
        for item in cart:
            if item["item"] == item_id:
                if item["quantity"] > 1:
                    item["quantity"] -= 1
                break
        return redirect("cart")