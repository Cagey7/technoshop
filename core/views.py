from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render


navbar_auth = [
    {"title":"Главная страница", "url_name": "index"},
    {"title":"Логин", "url_name": "login"},
    {"title":"Регистрация", "url_name": "register"},
]
navbar_not_auth = [
    {"title":"Главная страница", "url_name": "index"},
    {"title":"Выйти", "url_name": "logout"}
]


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def server_error(request):
    return HttpResponseServerError("<h1>Ошибка сервера</h1>")
