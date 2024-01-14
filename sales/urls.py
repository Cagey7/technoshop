from django.urls import path
from . import views

urlpatterns = [
    path("make_an_order/", views.MakeAnOrder.as_view(), name="make_an_order"),
    path("success/", views.SuccessOrder.as_view(), name="success"),
    path("order/<int:pk>/", views.OrderInfo.as_view(), name="order"),
]
