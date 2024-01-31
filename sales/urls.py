from django.urls import path
from . import views

urlpatterns = [
    path("make_an_order/", views.MakeAnOrder.as_view(), name="make_an_order"),
    path("order/<int:pk>/", views.OrderInfo.as_view(), name="order"),
    path("orders/", views.OrdersProfile.as_view(), name="orders"),
    path("cancel/<int:pk>/", views.CancelOrder.as_view(), name="cancel"),
]
