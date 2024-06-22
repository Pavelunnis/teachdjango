from django.shortcuts import render
from django.http import *
from django.template.response import TemplateResponse


def index(request):
    header = "Иностранные языки"
    list_langs = ["Английский", "Немецкий", "Испанский",
             "Французкий", "Итальянский"]
    user = {"name": "Максим,","age": 30}
    addr = ("Виноградная", 23, 45)
    data = {"header": header, "list_langs": list_langs}
    return render(request, "firstapp/index_app1.html", context=data)


def about(request):
    return HttpResponse("<h2>О Сайте</h2>")


def contact(request):
    return HttpResponseRedirect("/about") # временная переадресация | будет перенаправлять на /about
    # return HttpResponse("<h2>Контакты</h2>")


def products(request, productid=1):
    category = request.GET.get('cat', 'Не задана')
    output = '<h2>Продукт № {0} Категория №{1}</h2>'\
        .format(productid, category)
    return HttpResponse(output)


def users(request, id=1, name="Максим"):
    id = request.GET.get("id", "Не задано")
    name = request.GET.get('name', 'Не задано')
    output = "<h2>Пользователь</h2><h3>id: {0} Имя:{1}</h3>"\
        .format(id, name)
    return HttpResponse(output)


def details(request):
    return HttpResponsePermanentRedirect("/")
#постоянная переадресация | будет переадресация на корень(главную страницу)


#статусные коды

def access(request, age):
    if age not in range(1, 111):
        return HttpResponseBadRequest("Некорректные данные")
    if age>17:
        return HttpResponse("Доступ разрешен")
    else:
        return HttpResponseForbidden("Доступ заблокирован: недостаточно лет")
