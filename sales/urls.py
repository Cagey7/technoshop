from django.urls import path
from . import views

urlpatterns = [
    path("make_an_order/", views.MakeAnOrder.as_view(), name="make_an_order"),
]
