from django.shortcuts import render, redirect
from django.views import View
from users.models import Address
from cart.models import Cart, CartItem
from sales.models import Order, Purchase


class MakeAnOrder(View):
    def post(self, request, *args, **kwargs):
        user = self.request.user
        #TODO проверить если адрес у пользователя
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

        return redirect("cart")