from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *


urlpatterns = [
    path("login/", LoginUser.as_view(), name="login"),
    path("register/", RegisterUser.as_view(), name="register"),
    path("profile/", UserProfile.as_view(), name="profile"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("add_address/", AddAddress.as_view(), name="add_address"),
]
