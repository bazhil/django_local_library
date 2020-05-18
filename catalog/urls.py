# coding: utf-8

from django.conf.urls import *
from django.urls import path
from catalog.views import catalog, index


urlpatterns = [
    url(r'^$', catalog),
    path('', index, name='index'),
]