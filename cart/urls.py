from django.urls import path
from . import views

urlpatterns = [
    path('item/<int:item_id>/', views.AddToCart.as_view(), name='add-to-cart')
]
