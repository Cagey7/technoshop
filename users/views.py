from django.urls import reverse_lazy
from core.views import navbar_auth, navbar_not_auth
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from .forms import *


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name="users/login.html"
    redirect_authenticated_user = True
    extra_context = {
        "navbar_auth": navbar_auth,
        "navbar_not_auth": navbar_not_auth
    }

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "users/register.html"
    success_url = reverse_lazy("login")
    extra_context = {
        "navbar_auth": navbar_auth,
        "navbar_not_auth": navbar_not_auth
    }
