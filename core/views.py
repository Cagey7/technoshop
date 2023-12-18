from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render


navbar_auth = [
    {"title":"Главная страница", "url_name": "index", "selected": 0},
    {"title":"Логин", "url_name": "login", "selected": 0},
    {"title":"Регистрация", "url_name": "register", "selected": 0},
]
navbar_not_auth = [
    {"title":"Главная страница", "url_name": "index", "selected": 0},
    {"title":"Выйти", "url_name": "logout", "selected": 0}
]


def index(request):
    context = {
        "navbar_auth": navbar_auth,
        "navbar_not_auth": navbar_not_auth
    }
    return render(request, "core/index.html", context=context)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def server_error(request):
    return HttpResponseServerError("<h1>Ошибка сервера</h1>")
