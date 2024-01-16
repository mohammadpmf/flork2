from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Book

class BooksList(generic.ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'book_list.html'
    paginate_by = 4
    
class AddBook(generic.CreateView):
    model = Book
    template_name = 'book_new.html'
    fields = '__all__'
    success_url = reverse_lazy('book_list')