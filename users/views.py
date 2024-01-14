from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.views import View
from django.views.generic import TemplateView
from users.models import Address
from cart.models import Cart, CartItem
from sales.models import Order
from products.models import Item
from .forms import *
from django.urls import reverse_lazy
from core.views import navbar_auth, navbar_not_auth


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name="users/login.html"
    redirect_authenticated_user = True
    extra_context = {
        "navbar_auth": navbar_auth,
        "navbar_not_auth": navbar_not_auth
    }

    def form_valid(self, form):
        response = super().form_valid(form)
        cart = Cart.objects.get(user=self.request.user)
        if "cart" in self.request.session:
            session_cart = self.request.session["cart"]
            for session_item in session_cart:
                item = Item.objects.get(id=session_item["item"])
                if cart.item_in_cart(item.id):
                    cart_item = CartItem.objects.get(item=item, cart=cart)
                    quantity = session_item["quantity"] + cart_item.quantity
                    if quantity > item.quantity:
                        quantity = item.quantity
                    cart_item.quantity = quantity
                    cart_item.save()
                else:
                    quantity = session_item["quantity"]
                    new_cart_item = CartItem(item=item, cart=cart, quantity=quantity)
                    new_cart_item.save()
        return response


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "users/register.html"
    success_url = reverse_lazy("login")
    extra_context = {
        "navbar_auth": navbar_auth,
        "navbar_not_auth": navbar_not_auth
    }

    def form_valid(self, form):
        self.object = form.save()
        user_id = self.object.id
        cart = Cart(user_id=user_id)
        cart.save()
        return HttpResponseRedirect(self.get_success_url())


class AddAddress(View):
    def post(self, request, *args, **kwargs):
        address_input = request.POST.get("address")
        user = self.request.user
        Address.objects.filter(user=user).update(default=False)
        address = Address(user=user, info=address_input, default=True)
        address.save()
        return redirect("cart")


class UserProfile(TemplateView):
    template_name = "users/profile.html"
    extra_context = {
        "title": "Профиль",
        "navbar_auth": navbar_auth,
        "navbar_not_auth": navbar_not_auth,
    }

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["orders"] = Order.objects.filter(user=self.request.user)
        return context
