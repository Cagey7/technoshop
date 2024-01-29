from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms
from django.contrib.auth import get_user_model



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ("email",)


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Электронная почта", widget=forms.TextInput())
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ["username", "password"]


class RegisterUserForm(UserCreationForm):
    email = forms.CharField(label="Электронная почта", widget=forms.TextInput())
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ["email", "password1", "password2"]


class AddressForm(forms.Form):
    city = forms.CharField(min_length=2, max_length=63, label="Город", widget=forms.TextInput(attrs={"class": "form-control"}))
    street = forms.CharField(min_length=2, max_length=63, label="Улица", widget=forms.TextInput(attrs={"class": "form-control"}))
    house_number = forms.IntegerField(label="Номер дома", widget=forms.TextInput(attrs={"class": "form-control"}))
    apartment_number = forms.IntegerField(label="Номер квартиры", widget=forms.TextInput(attrs={"class": "form-control"}))
    