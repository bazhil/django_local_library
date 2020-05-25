# coding: utf-8

from django.conf.urls import *
from django.urls import path
from catalog.views import index, BookListView, BookDetailView, AuthorListView, AuthorDetailView, \
    LoanedBooksByUserListView, LoanedBooks, renew_book_librarian, AuthorCreate, AuthorUpdate, AuthorDelete



urlpatterns = [
    url(r'^$', index),
    url(r'^books/$', BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', BookDetailView.as_view(), name='book-detail'),
    url(r'^authors/$', AuthorListView.as_view(), name='authors'),
    url(r'^author/(?P<pk>\d+)$', AuthorDetailView.as_view(), name='author-detail'),
    url(r'^mybooks/$', LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    url(r'^borrowed-books/$', LoanedBooks.as_view(), name='borrowed-books'),
    url(r'^book/(?P<pk>[-\w]+)/renew/$', renew_book_librarian, name='renew-book-librarian'),
    url(r'^author/create/$', AuthorCreate.as_view(), name='author_create'),
    url(r'^author/(?P<pk>\d+)/update/$', AuthorUpdate.as_view(), name='author_update'),
    url(r'^author/(?P<pk>\d+)/delete/$', AuthorDelete.as_view(), name='author_delete'),
]