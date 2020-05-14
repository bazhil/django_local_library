# coding: utf-8

from django.conf.urls import *
from catalog.views import catalog


urlpatterns = [
    url(r'^$', catalog),
]