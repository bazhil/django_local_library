#  coding: utf-8


from django.template import loader, Context
from django.http import HttpResponse

import sys
sys.path.append('/home/user/PycharmProjects/locallibrary/catalog')
from catalog.models import Book


# Create your views here.

def catalog(request):
    books = Book.objects.all()
    t = loader.get_template("catalog.html")
    c = Context({'books': books})

    return HttpResponse(t.render(c.flatten()))


