from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from users.models import Address
from cart.models import Cart, CartItem
from sales.models import Order
from products.models import Item, Chapter
from .forms import *
from django.urls import reverse_lazy
from core.views import navbar_auth, navbar_not_auth


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name="users/login.html"
    redirect_authenticated_user = True
    extra_context = {
        "navbar_auth": navbar_auth,
        "navbar_not_auth": navbar_not_auth,
        "chapters": Chapter.objects.all(),
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
        "navbar_not_auth": navbar_not_auth,
        "chapters": Chapter.objects.all(),
    }

    def form_valid(self, form):
        self.object = form.save()
        user_id = self.object.id
        cart = Cart(user_id=user_id)
        cart.save()
        return HttpResponseRedirect(self.get_success_url())


class DeleteAddress(View):
    def post(self, request, *args, **kwargs):
        Address(id=request.POST.get("address")).delete()
        return redirect(self.get_success_url())

    def get_success_url(self):
        referer = self.request.META.get("HTTP_REFERER")
        if referer:
            return referer
        else:
            return reverse_lazy("index")


class AddressProfile(FormView):
    template_name = "users/address.html"
    form_class = AddressForm
    
    extra_context = {
        "title": "Профиль",
        "navbar_auth": navbar_auth,
        "navbar_not_auth": navbar_not_auth,
        "chapters": Chapter.objects.all(),
    }
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["addresses"] = Address.objects.filter(user=self.request.user)
        return context
    
    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        address_input = f'''г.{cleaned_data['city']} ул.{cleaned_data['street']} 
                        д.{cleaned_data['house_number']} кв.{cleaned_data['apartment_number']}'''
        user = self.request.user
        Address.objects.filter(user=user).update(default=False)
        address = Address(user=user, info=address_input, default=True)
        address.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        referer = self.request.META.get("HTTP_REFERER")
        if referer:
            return referer
        else:
            return reverse_lazy("index")


class UserProfile(TemplateView):
    template_name = "users/profile.html"

    extra_context = {
        "title": "Профиль",
        "navbar_auth": navbar_auth,
        "navbar_not_auth": navbar_not_auth,
        "chapters": Chapter.objects.all(),
    }


class ChangeFirstName(View):
    def post(self, request, *args, **kwargs):
        first_name = request.POST.get("first_name")
        self.request.user.first_name = first_name
        self.request.user.save()
        return redirect("user_profile")


class ChangeLastName(View):
    def post(self, request, *args, **kwargs):
        last_name = request.POST.get("last_name")
        print(last_name)
        self.request.user.last_name = last_name
        self.request.user.save()
        return redirect("user_profile")


class ChangePhoneNumber(View):
    def post(self, request, *args, **kwargs):
        phone_number = request.POST.get("phone_number")
        self.request.user.phone_number = phone_number
        self.request.user.save()
        return redirect("user_profile")
