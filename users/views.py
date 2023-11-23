from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from .forms import *


class LoginUser(LoginView):
    template_name="users/login.html"


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "users/register.html"
    success_url = reverse_lazy("login")