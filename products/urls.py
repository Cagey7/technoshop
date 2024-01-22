from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProductsHome.as_view(), name="index"),
    path("category/<slug:category_slug>", views.ItemCategory.as_view(), name="category"),
    path("item/<slug:item_slug>", views.ShowItem.as_view(), name="item"),
    path("chapter/<slug:chapter_slug>", views.ChapterInfo.as_view(), name="chapter"),
]
