from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render


navbar_auth = [
    {"title":"Корзина", "url_name": "cart"},
    {"title":"Логин", "url_name": "login"},
    {"title":"Регистрация", "url_name": "register"},
]
navbar_not_auth = [
    {"title":"Профиль", "url_name": "profile"},
    {"title":"Корзина", "url_name": "cart"},
    {"title":"Выйти", "url_name": "logout"}
]


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def server_error(request):
    return HttpResponseServerError("<h1>Ошибка сервера</h1>")
