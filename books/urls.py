from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.BooksList.as_view(), name='book_list'),
    path('new_book/', views.AddBook.as_view(), name='new_book'),
    path('detail/<int:pk>/', views.show_detail, name='detail'),
    path('update/<int:pk>/', views.UpdateBook.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeleteBook.as_view(), name='delete'),
]