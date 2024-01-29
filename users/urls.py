from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *


urlpatterns = [
    path("login/", LoginUser.as_view(), name="login"),
    path("register/", RegisterUser.as_view(), name="register"),
    path("address/", AddressProfile.as_view(), name="address"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("delete_address/", DeleteAddress.as_view(), name="delete_address"),
]
