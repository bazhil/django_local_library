# coding: utf-8

from django.conf.urls import *
from django.urls import path
from catalog.views import index, BookListView, BookDetailView



urlpatterns = [
    url(r'^$', index),
    url(r'^books/$', BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', BookDetailView.as_view(), name='book-detail'),
]