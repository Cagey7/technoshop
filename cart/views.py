from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import AddToCartForm
from .models import Cart, CartItem
from products.models import Item


class AddToCart(FormView):
    form_class = AddToCartForm

    def form_valid(self, form):
        item = Item.objects.get(id=self.kwargs["item_id"])
        quantity = form.cleaned_data["quantity"]
        if self.request.user.is_authenticated:
            cart = Cart.objects.get(user__id=self.request.user.id)
            cart_item = CartItem(quantity=quantity, cart=cart, item=item)
            cart_item.save()
        else:
            if not self.request.session.get("cart"):
                self.request.session["cart"] = []
            self.request.session["cart"].append({"item": item.id, "quantity": 1})
            print(self.request.session["cart"])
        return super().form_valid(form)
    
    def get_success_url(self):
        referer = self.request.META.get("HTTP_REFERER")
        if referer:
            return referer
        else:
            return reverse_lazy("index")