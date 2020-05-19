#  coding: utf-8


from django.template import loader, Context
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Book, Author, BookInstance, Genre
from django.views import generic


import sys
sys.path.append('/home/user/PycharmProjects/locallibrary/catalog')
from catalog.models import Book


# Create your views here.

# def catalog(request):
#     books = Book.objects.all()
#     t = loader.get_template("catalog.html")
#     c = Context({'books': books})
#
#     return HttpResponse(t.render(c.flatten()))


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



class BookListView(generic.ListView):
    model = Book
    paginate_by = 10

    def get_queryset(self):
        return Book.objects.filter(title__icontains='war')[:5]  # Получить 5 книг, содержащих 'war' в заголовке


    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(BookListView, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и иниуиализируем ее некоторым значением
        context['book_list'] = Book.objects.all()
        return context


class BookDetailView(generic.DetailView):
    model = Book

    def book_detail_view(request, pk):
        book_id=get_object_or_404(Book, pk=pk)

        return render(
            request,
            'catalog/book_detail.html',
            context={'book': book_id, }
        )