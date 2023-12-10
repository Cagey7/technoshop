from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render


def index(request):
    return render(request, "core/index.html")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def server_error(request):
    return HttpResponseServerError("<h1>Ошибка сервера</h1>")
