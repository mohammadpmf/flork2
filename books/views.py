from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .models import Book, Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class BooksList(generic.ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'book_list.html'
    paginate_by = 4
    
class AddBook(generic.CreateView):
    model = Book
    template_name = 'book_new.html'
    fields = ['title','author','translator','publisher','price','description','cover']
    # fields = '__all__'
    success_url = reverse_lazy('book_list')

def show_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    comments = Comment.objects.filter(book=book)
    context = {
        'book': book,
        'comments': comments,
    }
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        text = request.POST.get('text')
        Comment.objects.create(name=name, email=email, text=text, book=book)
    return render(request, 'book_detail.html', context)

class DeleteBook(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Book
    template_name = 'book_delete.html'
    success_url = reverse_lazy('book_list')

    def test_func(self):
        book = self.get_object()
        return book.owner == self.request.user


class UpdateBook(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Book
    template_name = 'book_new.html'
    fields = ['title','author','translator','publisher','price','description','cover']
    success_url = reverse_lazy('book_list')

    def test_func(self):
        book = self.get_object()
        return book.owner == self.request.user
