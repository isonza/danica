from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPage, name="mainpage"),
    path('book/', views.BookPage, name="book"),
]

"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPage, name="mainpage"),
    path('book/', views.BookPage, name="bookpage"),


    #path(r'^app//addDetail$', AddDetail, name="additem"),
    #path('next/', views.NewList, name'next'),
]
"""