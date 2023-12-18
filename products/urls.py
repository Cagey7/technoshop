from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProductsHome.as_view(), name="index"),
    path("category/<slug:category_slug>", views.ItemCategory.as_view(), name="category"),
]
