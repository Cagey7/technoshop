from django.urls import path
from . import views

urlpatterns = [
    path("item/<int:item_id>/", views.AddToCart.as_view(), name="add_to_cart"),
    path("cart/", views.CartPage.as_view(), name="cart"),
    path("delete_cart_item/<int:pk>/", views.DeleteItemCart.as_view(), name="delete_cart_item"),
    path("delete_cart_item_anon/<int:pk>/", views.DeleteItemCartAnon.as_view(), name="delete_cart_item_anon")
]
