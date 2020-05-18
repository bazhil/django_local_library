#  coding: utf-8


from django.template import loader, Context
from django.http import HttpResponse
from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre


import sys
sys.path.append('/home/user/PycharmProjects/locallibrary/catalog')
from catalog.models import Book


# Create your views here.

def catalog(request):
    books = Book.objects.all()
    t = loader.get_template("catalog.html")
    c = Context({'books': books})

    return HttpResponse(t.render(c.flatten()))


def index(request):
    """
        Функция отображения для домашней страницы сайта.
        """
    # Генерация "количеств" некоторых главных объектов
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Доступные книги (статус = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()  # Метод 'all()' применен по умолчанию.

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available, 'num_authors': num_authors},
    )


