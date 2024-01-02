from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.BooksList.as_view(), name='book_list'),
]
