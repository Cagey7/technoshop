from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from users.models import Address
from cart.models import Cart, CartItem
from sales.models import Order, Purchase
from core.views import navbar_auth, navbar_not_auth


class MakeAnOrder(View):
    def post(self, request, *args, **kwargs):
        user = self.request.user
        address = Address.objects.get(id=request.POST.get('address'))
        Address.objects.filter(user=user).update(default=False)
        Address(user=user, info=address, default=True)
        cart = Cart.objects.get(user=user)
        cart_items = CartItem.objects.filter(cart=cart)
        order = Order.objects.create(user=user, address=address)
        
        for cart_item in cart_items:
            Purchase.objects.create(order=order, quantity=cart_item.quantity, item=cart_item.item)
            cart_item.item.decrease_quantity(cart_item.quantity)
            cart_item.delete()

        return redirect("success")


class SuccessOrder(TemplateView):
    template_name = "sales/success.html"
    extra_context = {
        "title": "Спасибо за покупку",
        "navbar_auth": navbar_auth,
        "navbar_not_auth": navbar_not_auth,
    }


class OrderInfo(TemplateView):
    template_name = "sales/order.html"
    extra_context = {
        "title": "Спасибо за покупку",
        "navbar_auth": navbar_auth,
        "navbar_not_auth": navbar_not_auth,
    }
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["order"] = Order.objects.get(pk=kwargs.get("pk"))
        return context
