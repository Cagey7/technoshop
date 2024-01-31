from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.views.generic import RedirectView
from django.contrib import messages
from users.models import Address
from cart.models import Cart, CartItem
from sales.models import Order, Purchase
from products.models import Chapter
from core.views import navbar_auth, navbar_not_auth


class MakeAnOrder(View):
    def post(self, request, *args, **kwargs):
        user = self.request.user
        address = Address.objects.get(id=request.POST.get('address'))
        Address.objects.filter(user=user).update(default=False)
        Address(user=user, info=address, default=True)
        cart = Cart.objects.get(user=user)
        cart_items = CartItem.objects.filter(cart=cart)
        order = Order.objects.create(user=user, address=address, total=cart.get_total())
        
        for cart_item in cart_items:
            Purchase.objects.create(order=order, quantity=cart_item.quantity, item=cart_item.item)
            cart_item.item.decrease_quantity(cart_item.quantity)
            cart_item.delete()

        messages.success(request, "Спасибо за покупку")
        return redirect("index")



class OrderInfo(TemplateView):
    template_name = "sales/order.html"
    extra_context = {
        "title": "Спасибо за покупку",
        "navbar_auth": navbar_auth,
        "navbar_not_auth": navbar_not_auth,
        "chapters": Chapter.objects.all(),
    }
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["order"] = Order.objects.get(pk=kwargs.get("pk"))
        return context

class OrdersProfile(TemplateView):
    template_name = "sales/profile_orders.html"
    extra_context = {
        "title": "Профиль",
        "navbar_auth": navbar_auth,
        "navbar_not_auth": navbar_not_auth,
        "chapters": Chapter.objects.all(),
    }

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["orders"] = Order.objects.filter(user=self.request.user).order_by("-created")
        return context


class CancelOrder(View):
    def post(self, request, *args, **kwargs):
        order = Order.objects.get(id=kwargs.get("pk"))
        order.order_status = Order.Status.CANCELED
        order.save()
        return redirect("orders")
