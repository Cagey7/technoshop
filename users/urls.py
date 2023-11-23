from django.urls import include, path
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [
    path("login/", LoginUser.as_view(), name="login"),
    path("register/", RegisterUser.as_view(), name="register"),
]
