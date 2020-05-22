# coding: utf-8

from django.conf.urls import *
from django.urls import path
from catalog.views import index, BookListView, BookDetailView, AuthorListView, AuthorDetailView, LoanedBooksByUserListView



urlpatterns = [
    url(r'^$', index),
    url(r'^books/$', BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', BookDetailView.as_view(), name='book-detail'),
    url(r'^authors/$', AuthorListView.as_view(), name='authors'),
    url(r'^author/(?P<pk>\d+)$', AuthorDetailView.as_view(), name='author-detail'),
    url(r'^mybooks/$', LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]