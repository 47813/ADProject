from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

@api_view(['GET'])
def get_all_books_view(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response({'books': serializer.data})

@api_view(['GET'])
def get_books_by_author_view(request, author_name):
    books = Book.objects.filter(author__icontains=author_name)
    serializer = BookSerializer(books, many=True)
    return Response({'books': serializer.data})

@api_view(['GET'])
def get_books_by_title_keyword_view(request, keyword):
    books = Book.objects.filter(title__icontains=keyword)
    serializer = BookSerializer(books, many=True)
    return Response({'books': serializer.data})

@api_view(['GET'])
def get_books_ordered_by_title_view(request):
    books = Book.objects.order_by("title")
    serializer = BookSerializer(books, many=True)
    return Response({'books': serializer.data})