from django.shortcuts import render
from django.views import generic
from .models import Book

class BooksList(generic.ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'book_list.html'
    paginate_by = 4
    