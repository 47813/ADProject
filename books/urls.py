from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.get_all_books_view, name='all_books'),
    path('books/author/<str:author_name>/', views.get_books_by_author_view, name='books_by_author'),
    path('books/keyword/<str:keyword>/', views.get_books_by_title_keyword_view, name='books_by_keyword'),
    path('books/sorted/title/', views.get_books_ordered_by_title_view, name='books_ordered_title'),
]