from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms
from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email",)


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Электронная почта", widget=forms.TextInput())
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ["username", "password"]


class RegisterUserForm(UserCreationForm):
    email = forms.CharField(label="Электронная почта", widget=forms.TextInput())
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ["email", "password1", "password2"]
