from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from cart.models import Cart, CartItem
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
