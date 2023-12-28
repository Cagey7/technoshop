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
        cart = Cart.objects.get(user__id=self.request.user.id)
        cart_item = CartItem(quantity=quantity, cart=cart, item=item)
        cart_item.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        referer = self.request.META.get("HTTP_REFERER")
        if referer:
            return referer
        else:
            return reverse_lazy("index")